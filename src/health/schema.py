from pydantic import BaseModel


class Healthcheck(BaseModel):
    status: str
    checks: list
