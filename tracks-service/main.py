import fastapi
import app
import sys 
import base_library
import base_library.database
import contextlib
from app import crud, views

fastapi_app = fastapi.FastAPI(
    openapi_url=app.OPENAPI_URL,
    docs_url=app.DOCS_URL
)
    
@contextlib.asynccontextmanager
async def lifespan(app: fastapi.FastAPI):
    if '--reload-models' in sys.argv:
        await base_library.database.destroy_models()
    await base_library.database.init_models()
    yield
    base_library.database.destroy_connection()

fastapi_app.include_router(views.router)


