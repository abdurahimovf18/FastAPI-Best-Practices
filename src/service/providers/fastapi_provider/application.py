from fastapi import FastAPI

from .lifespan import lifespan


def create_instance() -> FastAPI:
    app = FastAPI(
        lifespan=lifespan,
        docs_url="/swagger",
    )

    return app
