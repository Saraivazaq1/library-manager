import os
from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

mssql_url = (
    f"mssql+pyodbc://{os.getenv('DB_SERVER')}/{os.getenv('DB_DATABASE')}"
    f"?driver={os.getenv('DB_DRIVER')}&trusted_connection=yes&TrustServerCertificate=yes"
)

engine = create_engine(mssql_url, echo=True)