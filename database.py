from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# PostgreSQL connection string (update with your credentials)
DATABASE_URL = "postgresql+psycopg2://postgres:SAMI%408149s@localhost:5432/logithon_db"


# Create database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for ORM models
Base = declarative_base()
