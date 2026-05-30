from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from .settings import settings

# ---------------------------------
#  DATABASE ENGINE
# --------------------------------
# Main connection between 
# FASt API ---> Postgres
engine = create_engine(
        settings.DATABASE_URL,
        echo=settings.DEBUG,
        pool_pre_ping=True
    )


# -------------------------
#  SESSION FACTORY
# --------------------------
# Creates new database sessions
SessionLocal = sessionmaker(
        autoflush=False,
        autocommit=False,
        bind=engine
    )


# -----------------
#  BASE MODEL
# -----------------
# Every Sqlalchemy model will inherit this
Base = declarative_base()


# -----------------------
#  DATABASE DEPENDENCY
# ------------------------

async def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
    