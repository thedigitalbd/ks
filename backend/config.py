import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://neondb_owner:npg_QWYXOSC3JhM9@ep-red-moon-a83h1tud-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "5fc6d8ab661706f61c16e1ddcf98a2778e259ec37b891e58d8b26e8ab8bf0d39af80844883ab5d63f5970741d5e2076efd3de1649acb47123daaa11f277332a1")


