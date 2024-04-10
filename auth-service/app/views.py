import fastapi
import schemas
import app
from app import crud

router = fastapi.APIRouter(prefix=f'{app.PREFIX}/books')


