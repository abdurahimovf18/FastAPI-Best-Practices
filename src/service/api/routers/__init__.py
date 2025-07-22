from fastapi import APIRouter

# importing all routers from files
from .rest import router as rest_router
from .ws import router as ws_router

application_router = APIRouter()

# ====================================
# Mount All Routers Declared At Files
# ====================================
application_router.include_router(rest_router)
application_router.include_router(ws_router)
