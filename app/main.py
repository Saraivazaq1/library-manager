from fastapi import FastAPI
from os import getenv
from dotenv import load_dotenv
from mssql_python import connect

load_dotenv()
conn = connect(getenv("SQL_CONNECTION_STRING"))

app = FastAPI()

@app.get("/")
def read_root():
    return {"Connection": "Started"}

