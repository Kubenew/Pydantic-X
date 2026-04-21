from fastapi import FastAPI
from pydantic_x import BaseModelX

app = FastAPI(title="Pydantic-X FastAPI Demo")


class RegisterUser(BaseModelX):
    username: str
    email: str

    class Config:
        sanitize = True
        strip_whitespace = True
        lowercase_email = True


@app.post("/register")
def register(payload: RegisterUser):
    return {"normalized": payload.model_dump()}
