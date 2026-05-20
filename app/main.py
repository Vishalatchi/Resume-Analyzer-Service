from fastapi import FastAPI
from app.api.routes.routes import router
from app.core.middleware import RequestLoggingMiddleware
from app.core.limiter import limiter
app = FastAPI(
    title="Resume Analyzer",
    version="1.0.0"
)
app.state.limiter=limiter
app.add_middleware(RequestLoggingMiddleware)
app.include_router(router)

@app.get("/health")
async def health_check():
    return{
        "status":"App is healthy"
    }

