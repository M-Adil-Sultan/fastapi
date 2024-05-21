from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from supabase import create_client, Client




DATABASE_URL = "https://enhsnxumzsejgkrvwwfs.supabase.co"
supabaseKey =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVuaHNueHVtenNlamdrcnZ3d2ZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTYzMjQ0NjgsImV4cCI6MjAzMTkwMDQ2OH0.cVRQI8OA854dbOZlvG03STBT_eGaPJZP3OPq5ADxR34"

supabase: Client = create_client(DATABASE_URL, supabaseKey)


# engine = create_engine(DATABASE_URL,supabaseKey)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
