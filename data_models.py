
from pydantic import BaseModel, Field


class Response(BaseModel):
    action: str = Field(description="could be either 'ping' or 'pong'")
