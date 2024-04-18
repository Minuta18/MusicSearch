import fastapi
import app
from app import crud
from app import schemas

router = fastapi.APIRouter(prefix=f'{app.PREFIX}/tracks')


