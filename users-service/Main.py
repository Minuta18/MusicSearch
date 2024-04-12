import fastapi
import app
import sys 
import base_library
import base_library.database
from app import crud, views

fastapi_app = fastapi.FastAPI(
    openapi_url=app.OPENAPI_URL,
    docs_url=app.DOCS_URL
)

@fastapi.on_event('startup')
async def startup_event():
    if '--reload-models' in sys.argv:
        await base_library.database.destroy_models()
    await base_library.database.init_models()

@fastapi.on_event('shutdown')
async def shutdown_event():
    await base_library.database.destroy_connection()

fastapi_app.include_router(views.router)


