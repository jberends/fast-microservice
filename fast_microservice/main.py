from application import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8888,
                log_level="info", reload=True)
