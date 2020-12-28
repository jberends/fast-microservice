import router_echo
import router_root

from fast_microservice.application import app

app.include_router(router_echo.router)
app.include_router(router_root.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8888, log_level="info", reload=True)
