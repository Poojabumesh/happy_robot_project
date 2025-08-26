def verify_mc_number(mc_number: str, api_key: str) -> dict:
    import requests

    url = f"https://mobile.fmcsa.dot.gov/qc/services/carriers/{mc_number}?webKey={api_key}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"status": "error", "message": f"FMCSA API error {response.status_code}", "authorized": False}

    data = response.json()
    content = data.get("content")

    if not content:
        return {
            "status": "invalid",
            "message": "MC number not found or not active",
            "authorized": False
        }

    try:
        carrier_info = content[0]
        return {
            "status": carrier_info.get("status", "Unknown"),
            "carrierOperation": carrier_info.get("carrierOperation", "Unknown"),
            "legalName": carrier_info.get("legalName", "Unknown"),
            "authorized": carrier_info.get("status", "").lower() == "active"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Unexpected error: {str(e)}",
            "authorized": False
        }
