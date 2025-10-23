import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')

    # You can add validation
    if not EMAIL or not PASSWORD:
        raise ValueError("EMAIL and PASSWORD must be set in .env file")

print(f"Email: {os.getenv('EMAIL')}")
print(f"Password: {os.getenv('PASSWORD')}")