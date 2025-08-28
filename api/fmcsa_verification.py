import requests

def verify_mc_number(mc_number: str, api_key: str) -> dict:
    url = f"https://mobile.fmcsa.dot.gov/qc/services/carriers/{mc_number}?webKey={api_key}"
    print(f"➡️ Requesting FMCSA: {url}")
    print("Using FMCSA API key:", api_key)    

    try:
        response = requests.get(url)
        print("⬅️ Status Code:", response.status_code)
        print("⬅️ Response Text:", response.text)

        if response.status_code != 200:
            return {
                "status": "error",
                "message": f"FMCSA API error {response.status_code}",
                "authorized": False
            }

        data = response.json()
        carrier_info = data.get("content", {}).get("carrier")

        if not carrier_info:
            return {
                "status": "invalid",
                "message": "MC number not found or no carrier data.",
                "authorized": False
            }

        status_code = carrier_info.get("statusCode", "").upper()
        legal_name = carrier_info.get("legalName", "Unknown")
        operation_desc = carrier_info.get("carrierOperation", {}).get("carrierOperationDesc", "Unknown")

        return {
            "status": status_code,
            "legalName": legal_name,
            "carrierOperation": operation_desc,
            "authorized": status_code == "A"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Unexpected error: {str(e)}",
            "authorized": False
        }
