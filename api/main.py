from fastapi import FastAPI, Request, HTTPException
from .load_matcher import load_available
from .fmcsa_verification import verify_mc_number
from utils.secrets import load_api_key
from pydantic import BaseModel

app = FastAPI()

API_KEY = load_api_key()
print("🎯 Render picked up API_KEY:", load_api_key()) 
API_KEY_NAME = "x-api-key"

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    api_key = request.headers.get(API_KEY_NAME)
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return await call_next(request)

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
    result = verify_mc_number(mc_number, API_KEY)
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
