import os

class Config:
    # NeonDB PostgreSQL connection URL
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", 
        "postgresql://neondb_owner:npg_QWYXOSC3JhM9@ep-red-moon-a83h1tud-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")

