from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags= ['Blog']
)
get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowBlog])
def all( db: Session= Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session= Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session= Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(db, id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session= Depends(get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, db, request)

@router.get('/{id}', status_code=200, response_model = schemas.ShowBlog)
def show(id, db: Session= Depends(get_db), status_code=200, get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)