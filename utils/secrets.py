def load_api_key(filepath="utils/api_key.txt"):
    with open(filepath, "r") as f:
        return f.read().strip()
