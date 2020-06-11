from typing import List

from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/v1"
    SECRET_KEY: str = "123"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = ""
    SERVER_HOST: AnyHttpUrl = "http://localhost"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost",
        "http://localhost:4200",
        "http://localhost:3000",
        "http://localhost:8080",
    ]

    PROJECT_NAME: str = "kalaam"

    class Config:
        case_sensitive = True


settings = Settings()
