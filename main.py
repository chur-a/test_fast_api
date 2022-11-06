import uvicorn

from fastapi import FastAPI

from src.api.resources import router
from src.config import config


app = FastAPI(
    title=config.PROJECT_NAME,
    version=config.VERSION,
    openapi_url="/docs/openapi.json"
)


@app.get("/")
def root():
    return {"service": config.PROJECT_NAME, "version": config.VERSION}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
