from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
import os
from common.authentication import DatabricksAuthentication
from fastapi import Header

catalog = os.getenv("DATABRICKS_REFERENCE_CATALOG")
schema = os.getenv("DATABRICKS_REFERENCE_SCHEMA")

def get_databricks_connection(bearer: str = None):
    return DatabricksAuthentication(bearer=bearer).client

pool_args = {
    "pool_recycle": 5,
    "pool_size": 10,
    "max_overflow": 15,
    "pool_pre_ping": True,
}

def create_engine_with_catalog_schema(bearer: str = None):
    engine = create_engine(
        f"databricks://",
        creator=lambda: get_databricks_connection(bearer),
        **pool_args
    )
    
    @event.listens_for(engine, "connect")
    def set_catalog_schema(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute(f"BEGIN USE CATALOG {catalog};USE SCHEMA {schema}; END")
        cursor.close()
    
    return engine

def get_db(bearer: str):
    print(bearer)
    
    # Create a new engine with the bearer token
    bearer_engine = create_engine_with_catalog_schema(bearer)
    
    # Create a new session with the bearer-specific engine
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=bearer_engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 