import psycopg2
from os import getenv
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env

conn = psycopg2.connect(host=getenv("HOST"), database=getenv("DATABASE_NAME"), 
    user=getenv("DATABASE_USER"), password=getenv("DATABASE_PASS"), port=getenv("PORT"))
