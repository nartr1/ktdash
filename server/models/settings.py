from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    message: str = "Welcome to KTDash!"
    host: str = "127.0.0.1"
    port: int = 8000
    
    db_name: str = ""
    db_url: str = ""
    db_port: int = 3306

    hot_reload: bool = False
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env.dev", extra="allow")

SETTINGS = Settings()
