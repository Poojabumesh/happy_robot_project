from fastapi import FastAPI, Request
from .load_matcher import load_available
from .fmcsa_verification import verify_mc_number
from utils.secrets import load_api_key
from pydantic import BaseModel

app = FastAPI()

class MCRequest(BaseModel):
    mc_number : str

class LoadMatchRequest(BaseModel):
    origin: str
    destination: str
    equipment_type: str

# Health check
@app.get("/")
def root():
    return {"status": "running"}

# Verify MC number
@app.post("/verify_mc")
async def verify_mc(data: MCRequest):
    mc_number = data.mc_number

    api_key = load_api_key()
    result = verify_mc_number(mc_number, api_key)
    return result

# Match available load
@app.post("/match_load")
async def match_load(data: LoadMatchRequest):
    origin = data.origin
    destination = data.destination
    equipment_type = data.equipment_type

    loads = load_available("data/loads.csv", origin, destination, equipment_type)

    if not loads:
        return {"found": False, "message": "No matching loads"}

    top_load = loads[0]
    return {
        "found": True,
        "load_id": top_load["load_id"],
        "origin": top_load["origin"],
        "destination": top_load["destination"],
        "pickup_datetime": top_load["pickup_datetime"],
        "delivery_datetime": top_load["delivery_datetime"],
        "equipment_type": top_load["equipment_type"],
        "rate": top_load["loadboard_rate"],
        "notes": top_load["notes"],
        "commodity": top_load["commodity_type"],
        "weight": top_load["weight"]
    }
