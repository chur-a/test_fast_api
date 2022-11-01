from src.api.resources import router

import uvicorn

from fastapi import FastAPI


app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
