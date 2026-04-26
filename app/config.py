from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int
    DATABASE_URL:str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings=Settings() # basically this is the way to read the values from env

SECRET_KEY=settings.SECRET
ALGORITHM=settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES=settings.ACCESS_TOKEN_EXPIRE_MINUTES
DATABASE_URL=settings.DATABASE_URL
