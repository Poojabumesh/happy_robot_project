import os
from dotenv import load_dotenv

load_dotenv()

def load_api_key():
    return os.getenv("API_KEY")


