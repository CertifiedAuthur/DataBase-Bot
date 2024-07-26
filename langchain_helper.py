from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
import os
from few_shots import few_shots
from dotenv import load_dotenv

load_dotenv()

def get_few_shot_db_chain():
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["api_key"], temperature=0.1)
    db_user = "root"
    db_password = "6877"
    db_host = "localhost"
    db_name = "atliq_tshirts"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}", sample_rows_in_table_info=3)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2  # this means pull me two example. k can be any number
    )
    
    example_prompt = PromptTemplate(
    input_variables = ["Question", "SQLQuery", "SQLResult", "Answer",],
    template =  "\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )
    
    few_shot_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    prefix = _mysql_prompt,
    suffix = PROMPT_SUFFIX,
    input_variables = ["input", "table_info", "top_k"] # these variables are used in the prefix
    )

    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt = few_shot_prompt)
    return chain

if __name__ == "__main__":
    chain = get_few_shot_db_chain()
    print(chain.run("How many total t shirts are left in total in stock?"))