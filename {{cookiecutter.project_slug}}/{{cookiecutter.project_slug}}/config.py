from pydantic import BaseSettings


class Config(BaseSettings):
    verbose: bool = False
    host: str = '127.0.0.1'
    port: int = 9000
