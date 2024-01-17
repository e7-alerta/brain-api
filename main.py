import sentry_sdk
from fastapi import FastAPI

from web.routes.address.address import address_routes

sentry_sdk.init(
    dsn="https://e4ccbeedd1f6647c9355684d20f30ee0@o4506585080004608.ingest.sentry.io/4506586794557440",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

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
