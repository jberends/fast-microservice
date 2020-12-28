from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse, name="home")
async def get_root() -> str:
    """Echo the content of the body. """
    return """
    <html>
        <head>
            <title>
                Some knowledge required.
            </title>
        </head>
        <body>
            <h1>
                Hello World!
            </h1>
        </body>
    </html>
    """
