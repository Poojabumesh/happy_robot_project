import os

def load_api_key():
    print("Render API_Key:", os.getenv("API_KEY"))
    return os.getenv("API_KEY")


