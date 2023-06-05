import random
from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import services
import dependencies
import models
import schemas
from database import engine
models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix='',
)
@router.get('/')
def hello_capy():
    return FileResponse("index.html")

@router.get('/capys', response_model=list[schemas.Capy])
def all_capys(db: Session = Depends(dependencies.get_db)):
    capys = services.capys.get_capys(db)
    return capys



@router.get('/capys/random')
def get_capy_by_id(
        db: Session = Depends(dependencies.get_db)
):
    capys = services.capys.get_capys(db)
    capy_id=random.randint(1,len(capys))
    return services.capys.get_capy_by_id(db, capy_id)



@router.get('/capys/{capy_id}', response_model=schemas.Capy)
def get_capy_by_id(
        capy_id: int,
        db: Session = Depends(dependencies.get_db)
):
    return services.capys.get_capy_by_id(db, capy_id)

@router.get('/capys/{capy_id}/img')
def get_img_by_id(
        capy_id: int,
        db: Session = Depends(dependencies.get_db)
):
    return services.capys.get_img_by_id(db, capy_id)

@router.post('/capys', response_model=schemas.Capy)
def add_capy(
        capy: schemas.CapyToCreate,
        db: Session = Depends(dependencies.get_db),
):
    return services.capys.add_capy(db, capy)

@router.delete('/capys/{capy_id}')
def delete_capy(
        capy_id: int,
        db: Session = Depends(dependencies.get_db)
):
    return services.capys.delete_capy(db, capy_id)


@router.put('/capys/{capy_id}')
def update_capy(
        capy_id: int,
        capy: schemas.CapyToCreate,
        db: Session = Depends(dependencies.get_db)
):
    return services.capys.update_capy(db, capy_id, capy)

