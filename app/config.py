from pydantic import BaseSettings


# Settings class for environment variable
class Settings(BaseSettings):
    app_name: str = "Carbon Gallery Backend"
    database_connection_url: str

    class Config:
        env_file = ".env"


settings = Settings()