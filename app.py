from fastapi import FastAPI,APIRouter
from api.graph import router as graph_router

app = FastAPI()
api_router = APIRouter(prefix="/api")
api_router.include_router(graph_router, prefix="/graph", tags=["graph"])
app.include_router(api_router)


@app.get("/v1/health")
async def health_check():
    return {"status": "healthy"}
