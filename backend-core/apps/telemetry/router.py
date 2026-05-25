from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TelemetryData(BaseModel):
    water_level: float
    soil_moisture: float
    temperature: float

@router.post("/")
async def receive_telemetry(data: TelemetryData):
    return {
        "status": "success",
        "message": "Telemetry received successfully",
        "received_data": data.dict()
    }