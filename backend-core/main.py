from fastapi import FastAPI
from apps.telemetry.router import router as telemetry_router
from apps.communications.router import router as comms_router
from apps.analytics.router import router as analytics_router

app = FastAPI(title="JalRakshak API", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    # Initialize DB connection, etc.
    pass

app.include_router(telemetry_router, prefix="/api/v1/telemetry", tags=["Telemetry"])
app.include_router(comms_router, prefix="/api/v1/comms", tags=["Communications"])
app.include_router(analytics_router, prefix="/api/v1/analytics", tags=["Analytics"])

@app.get("/")
async def root():
    return {"status": "online", "message": "JalRakshak Gateway"}
