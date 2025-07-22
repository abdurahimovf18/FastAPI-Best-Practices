from src.service.providers.fastapi_provider import create_instance

# All REST and WebSocket routes grouped here
from .routers import application_router

app = create_instance()
app.include_router(application_router)
