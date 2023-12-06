from fastapi import Depends, APIRouter




router = APIRouter()


@router.get('/')
def index():
    return {'ok': True}