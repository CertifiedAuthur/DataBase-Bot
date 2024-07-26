# DataBase-tshirts-Bot

#### AtliQ T-Shirts Database Q&A 👕
This project demonstrates how to build a Q&A system for querying a T-shirt inventory database using a combination of Google Generative AI, SQLDatabase, and LangChain libraries. The system is designed to provide natural language answers to queries about T-shirt inventory, using few-shot learning and semantic similarity for improved accuracy.

###### Table of Contents
Features
Installation
Usage
Few-Shot Examples
Project Structure
Dependencies
License
Features

Query a T-shirt inventory database using natural language.
Few-shot learning with semantic similarity example selection for improved query responses.
Streamlit interface for easy interaction.
Integration with Google Generative AI for natural language processing.
Use of SQLAlchemy for database interaction and LangChain for NLP tasks.

##### Installation
Clone the repository:
git clone https://github.com/CertifiedAuthur/database-tshirts-bot.git
cd database-tshirts-bot

###### Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

###### Install the required packages:
pip install -r requirements.txt

###### Set up environment variables:
Create a .env file in the project root and add your Google API key:
api_key=YOUR_GOOGLE_API_KEY
Usage

###### Run the main script:
python main.py

##### Interact with the Streamlit interface:
streamlit run streamlit_app.py
Ask questions about your T-shirt inventory:
Enter a question in the Streamlit app and get answers based on the database.

##### Few-Shot Examples
The project uses few-shot examples to guide the AI in generating accurate SQL queries and results. Below are some example prompts used in the system:

few_shots = [
   {'Question': "How many t-shirts do we have left for the nike in extra small size and white color?",
    'SQLQuery': "SELECT SUM(stock_quantity ) FROM t_shirts WHERE brand = 'Nike' AND color = 'White' AND size = 'XS'",
    'SQLResult': "Result of the SQL query",
    'Answer': '10'},
    {'Question': "How much is the price of the inventory for all small size t-shirts?",
    'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
    'SQLResult': "Result of the SQL query",
    'Answer': '20068'},
    {'Question': "If we have to sell all the Levi's T-shirts today with discounts applied. How much revenue our store will generate (post discounts)?",
    'SQLQuery': """
    SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount, 0))/100)) as total_revenue
    FROM (SELECT sum(price*stock_quantity) as total_amount, t_shirt_id 
          FROM t_shirts WHERE brand = 'Levi'
          GROUP BY t_shirt_id) a 
    LEFT JOIN discounts on a.t_shirt_id = discounts.t_shirt_id
    """,
    'SQLResult': "Result of the SQL query",
    'Answer': '25434.7'},
    {'Question': "If we have to sell all the Levi's T-shirts today. How much revenue our store will get?",
    'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
    'SQLResult': "Result of the SQL query",
    'Answer': '28811'},
    {'Question': "How many white color Levi's t_shirts we have available?",
    'SQLQuery': """
    SELECT SUM(stock_quantity )
    FROM t_shirts 
    WHERE brand = 'Levi' AND color = 'White'
    """,
    'SQLResult': "Result of the SQL query",
    'Answer': '253'},
]

##### Project Structure
.
├── few_shots.py                 # Contains few-shot examples
├── main.py                      # Main script to run the project
├── streamlit_app.py             # Streamlit interface for interaction
├── requirements.txt             # Required packages
├── .env                         # Environment variables
└── README.md                    # This README file

##### Dependencies
langchain-google-genai
langchain-community-utilities
langchain-experimental-sql
langchain-huggingface
langchain-community-vectorstores
sqlalchemy
streamlit
python-dotenv
pymysql


##### Install all dependencies using the command:
pip install -r requirements.txt

License
This project is licensed under the MIT License.
