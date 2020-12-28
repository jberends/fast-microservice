from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EchoResult(BaseModel):
    """Echo response model."""

    echo: str


@router.post("/echo", response_model=EchoResult, name="echo")
def post_echo(body: str) -> EchoResult:
    """Echo the content of the body. """
    return EchoResult(echo=body)
