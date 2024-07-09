Generative AI App for Database Insights
This project is a generative AI application that allows users to get insights from local databases such as MySQL using simple natural language queries.

Table of Contents
Introduction
Features
Prerequisites
Installation
Usage
Acknowledgements
Introduction
This project leverages Flask for the backend, a variety of AI and machine learning libraries for generating responses, and a simple frontend interface to interact with the app. Users can query their local databases and get meaningful insights without needing to know SQL.

Features
Simple natural language queries to extract data from local databases.
Integration with MySQL or other relational databases.
AI-generated responses using Claude API.
Prerequisites
Node.js and npm (for frontend)
Python 3.10.0 or higher (for backend)
MySQL or any other supported relational database
Installation
Backend
Clone the repository:
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the backend dependencies:
pip install -r requirements.txt
Set up your environment variables in a .env file:
DB_URL=your_database_url
CLAUDE_API_KEY=your_claude_api_key

Start the backend server:
python app1.py
Frontend
Navigate to the frontend directory:
Install the frontend dependencies:
npm install
Start the frontend server:
npm start

Here's a README file for your GitHub project:

Generative AI App for Database Insights
This project is a generative AI application that allows users to get insights from local databases such as MySQL using simple natural language queries.

Table of Contents
Introduction
Features
Prerequisites
Installation
Usage
Acknowledgements
Introduction
This project leverages Flask for the backend, a variety of AI and machine learning libraries for generating responses, and a simple frontend interface to interact with the app. Users can query their local databases and get meaningful insights without needing to know SQL.

Features
Simple natural language queries to extract data from local databases.
Integration with MySQL or other relational databases.
AI-generated responses using Claude API.
Prerequisites
Node.js and npm (for frontend)
Python 3.10.0 or higher (for backend)
MySQL or any other supported relational database
Installation
Backend
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the backend dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your environment variables in a .env file:

env
Copy code
DB_URL=your_database_url
CLAUDE_API_KEY=your_claude_api_key
Start the backend server:

bash
Copy code
python app1.py
Frontend
Navigate to the frontend directory:

bash
Copy code
cd frontend
Install the frontend dependencies:

bash
Copy code
npm install
Start the frontend server:

bash
Copy code
npm start
Usage
Ensure both the frontend and backend servers are running.
Access the frontend interface through your browser at http://localhost:3000.
Enter your natural language query to interact with the database and receive AI-generated insights.
Acknowledgements
Special thanks to @AnthropicAI! and @alexalbert__ for creating the opportunity to showcase this project.

Dependencies
The backend dependencies are listed in requirements.txt:
aiohttp==3.9.5
aiosignal==1.3.1
annotated-types==0.7.0
anthropic==0.30.1
anyio==4.4.0
async-timeout==4.0.3
attrs==23.2.0
blinker==1.8.2
certifi==2024.7.4
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
dataclasses-json==0.6.7
distro==1.9.0
exceptiongroup==1.2.1
faiss-cpu==1.8.0.post1
filelock==3.15.4
Flask==3.0.3
Flask-Cors==4.0.1
frozenlist==1.4.1
fsspec==2024.6.1
greenlet==3.0.3
h11==0.14.0
httpcore==1.0.5
httpx==0.27.0
huggingface-hub==0.23.4
idna==3.7
intel-openmp==2021.4.0
itsdangerous==2.2.0
Jinja2==3.1.4
jiter==0.5.0
joblib==1.4.2
jsonpatch==1.33
jsonpointer==3.0.0
langchain==0.2.7
langchain-community==0.2.7
langchain-core==0.2.12
langchain-huggingface==0.0.3
langchain-text-splitters==0.2.2
langsmith==0.1.84
MarkupSafe==2.1.5
marshmallow==3.21.3
mkl==2021.4.0
mpmath==1.3.0
multidict==6.0.5
mypy-extensions==1.0.0
mysqlclient==2.2.4
networkx==3.3
numpy==1.26.4
orjson==3.10.6
packaging==24.1
pillow==10.4.0
pydantic==2.8.2
pydantic_core==2.20.1
PyMySQL==1.1.1
python-dotenv==1.0.1
PyYAML==6.0.1
regex==2024.5.15
requests==2.32.3
safetensors==0.4.3
scikit-learn==1.5.1
scipy==1.14.0
sentence-transformers==3.0.1
sniffio==1.3.1
SQLAlchemy==2.0.31
sympy==1.13.0
tbb==2021.13.0
tenacity==8.5.0
threadpoolctl==3.5.0
tokenizers==0.19.1
torch==2.3.1
tqdm==4.66.4
transformers==4.42.3
typing-inspect==0.9.0
typing_extensions==4.12.2
urllib3==2.2.2
Werkzeug==3.0.3
yarl==1.9.4
