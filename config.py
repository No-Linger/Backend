import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    DATABSE_URL = os.getenv("DATABASE_URL")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    SERVICE_ACCOUNT_KEY = os.getenv("SERVICE_ACCOUNT_KEY")