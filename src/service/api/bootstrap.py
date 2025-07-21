from src.service.providers.fastapi_provider import create_instance

from .routers import router

# creating a FastAPI instance
app = create_instance()

# Registering router
app.include_router(router)
