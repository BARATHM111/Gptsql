import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text, inspect
from dotenv import load_dotenv
import json
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from datetime import datetime, date
import re
import requests  # To make HTTP requests to Claude API

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Database connection
db_url = os.getenv('DB_URL')
if db_url is None:
    raise ValueError("DB_URL environment variable is not set")

try:
    engine = create_engine(db_url)
except ModuleNotFoundError:
    print("mysqlclient not found, attempting to use pymysql")
    db_url = db_url.replace('mysql://', 'mysql+pymysql://')
    engine = create_engine(db_url)

# Test the database connection and get schema information
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful")

        # Get list of tables
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print("Available tables:", tables)

        # If tables exist, print columns of the first table
        if tables:
            columns = inspector.get_columns(tables[0])
            print(f"Columns in table '{tables[0]}':")
            for column in columns:
                print(f"- {column['name']} ({column['type']})")
except Exception as e:
    print(f"Error connecting to the database: {e}")
    raise

# Initialize Claude client
API_KEY = os.getenv('CLAUDE_API_KEY')
if API_KEY is None:
    raise ValueError("CLAUDE_API_KEY environment variable is not set")

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Initialize RAG components
embeddings = HuggingFaceEmbeddings()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
vectorstore = None

def initialize_rag():
    global vectorstore
    try:
        # Fetch data from database
        with engine.connect() as connection:
            if tables:
                data = []
                for table in tables:
                    query = f"SELECT * FROM {table} LIMIT 100"  # Fetch 100 rows from each table
                    result = connection.execute(text(query))
                    table_data = [f"Table: {table}, " + ", ".join(f"{k}: {v}" for k, v in row._mapping.items()) for row in result]
                    data.extend(table_data)
            else:
                raise ValueError("No tables found in the database")
        
        # Create document chunks
        texts = text_splitter.split_text("\n".join(data))
        
        # Create vector store
        vectorstore = FAISS.from_texts(texts, embeddings)
        print("RAG system initialized successfully")
    except Exception as e:
        print(f"Error initializing RAG system: {e}")
        raise

# Initialize RAG on startup
initialize_rag()

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f'Type {type(obj)} not serializable')

def get_relevant_data(user_input):
    # Extract table name from user input
    match = re.search(r'\b(\w+)\b', user_input)
    if match:
        potential_table = match.group(1)
        if potential_table in tables:
            with engine.connect() as connection:
                # Get row count
                count_query = f"SELECT COUNT(*) FROM {potential_table}"
                row_count = connection.execute(text(count_query)).scalar()
                
                # Get sample data
                sample_query = f"SELECT * FROM {potential_table} LIMIT 5"
                result = connection.execute(text(sample_query))
                sample_data = [dict(row._mapping) for row in result]
                
                return {
                    "table": potential_table,
                    "row_count": row_count,
                    "sample_data": sample_data
                }
    
    # If no specific table is mentioned or found, return a summary of all tables
    summary = {}
    with engine.connect() as connection:
        for table in tables:
            count_query = f"SELECT COUNT(*) FROM {table}"
            row_count = connection.execute(text(count_query)).scalar()
            summary[table] = {"row_count": row_count}
    
    return {"summary": summary}

@app.route('/')
def home():
    return "Hello, World! Flask server is running."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json['message']
        
        # Use RAG to retrieve relevant information
        if vectorstore:
            relevant_docs = vectorstore.similarity_search(user_input, k=2)
            context = "\n".join([doc.page_content for doc in relevant_docs])
        else:
            context = "No context available."
        
        # Get relevant data based on user input
        relevant_data = get_relevant_data(user_input)
        
        messages = [
            {"role": "system", "content": "You are a database assistant. Provide concise answers based on the given data."},
            {"role": "user", "content": f"Database info: {json.dumps(relevant_data, default=json_serial)}"},
            {"role": "user", "content": f"Context: {context[:300]}"},
            {"role": "user", "content": user_input}
        ]

        # Call Claude API
        payload = {
            "model": "claude-v1",  # Replace with the actual model ID if different
            "messages": messages
        }
        
        response = requests.post('https://api.anthropic.com/v1/complete', headers=headers, json=payload)  # Update URL
        response.raise_for_status()
        completion = response.json()
        ai_response = completion['choices'][0]['message']['content']
        
        return jsonify({"response": ai_response})

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/refresh_rag', methods=['POST'])
def refresh_rag():
    try:
        initialize_rag()
        return jsonify({"message": "RAG system refreshed successfully"}), 200
    except Exception as e:
        app.logger.error(f"Failed to refresh RAG: {str(e)}")
        return jsonify({"error": "Failed to refresh RAG system"}), 500

if __name__ == '__main__':
    app.run(debug=True)
