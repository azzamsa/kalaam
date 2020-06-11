from app.config import settings
from app.user.controller import router as user_router
from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

__version__ = "0.1.0"

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

api_router = APIRouter()
api_router.include_router(user_router, prefix="/users", tags=["users"])


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
