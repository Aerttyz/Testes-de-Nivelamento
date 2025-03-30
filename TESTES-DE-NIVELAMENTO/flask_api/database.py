from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

