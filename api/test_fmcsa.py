import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fmcsa_verification import verify_mc_number
from utils.secrets import load_api_key

if __name__ == "__main__":
    api_key = load_api_key()

    mc = input("Enter MC number: ").strip()
    result = verify_mc_number(mc, api_key)

    if result.get("authorized"):
        print(f"Authorized Carrier: {result['legalName']} ({result['carrierOperation']})")
    else:
        print(f"Unauthorized or Invalid MC Number. Status: {result.get('status')}")
    
    print(f"📦 Name: {result.get('legalName')}")
    print(f"🚛 Operation: {result.get('carrierOperation')}")
