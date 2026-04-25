from fastapi import FastAPI

from src.api import health, contacts
from src.conf.config import config
from src.conf.constants import API_PREFIX

app = FastAPI(title="Contacts API")

app.include_router(health.router, prefix=API_PREFIX)
app.include_router(contacts.router, prefix=API_PREFIX)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=config.APP_HOST,
        port=config.APP_PORT,
        reload=True,
    )

