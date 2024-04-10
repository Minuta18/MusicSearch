import fastapi
import app
import sys 
from app import crud, views

fastapi_app = fastapi.FastAPI(
    openapi_url=app.OPENAPI_URL,
    docs_url=app.DOCS_URL
)

@fastapi.on_event('startup')
async def startup_event():
    if '--reload-models' in sys.argv:
        await crud.destroy_models()
    await crud.init_models()

@fastapi.on_event('shutdown')
async def shutdown_event():
    await app.engine.dispose()

fastapi_app.include_router(views.router)


