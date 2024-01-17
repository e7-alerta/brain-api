from fastapi import FastAPI

from web.routes.address.address import address_routes

app = FastAPI()
app.include_router(address_routes)

APP_NAME = "brain-api"
APP_VERSION = "1.0.1"

@app.get("/")
async def root():
    return {
        "message": f"Hello {APP_NAME} v{APP_VERSION}"
    }


@app.get("/version")
async def say_hello():
    return {
        "version": APP_VERSION,
        "app": APP_NAME
    }
