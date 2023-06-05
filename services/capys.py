from sqlalchemy.orm import Session

import models
import schemas

def add_capy(db: Session, capy: schemas.CapyToCreate):
    db_capy = models.CapyInDB(
        name=capy.name,
        description=capy.description,
        photo=capy.photo
    )

    db.add(db_capy)
    db.commit()
    db.refresh(db_capy)
    return db_capy

def get_capy_by_id(db: Session, capy_id: int):
    capy = db.query(models.CapyInDB).filter(
        models.CapyInDB.id == capy_id
    ).first()
    return capy

def get_img_by_id(db: Session, capy_id: int):
    capy = db.query(models.CapyInDB).filter(
        models.CapyInDB.id == capy_id
    ).first()
    return capy.photo

def get_capys(db: Session):
    return db.query(models.CapyInDB).all()

def update_capy(db: Session, capy_id: int, new_capy: schemas.CapyToCreate):
    capy = get_capy_by_id(db, capy_id)
    capy.name = new_capy.name
    capy.description=new_capy.description
    capy.photo=new_capy.photo
    db.commit()
    db.refresh(capy_id)
    return capy

def delete_capy(db: Session, capy_id: int):
    capy = db.query(models.CapyInDB).filter(
        models.CapyInDB.id == capy_id
    ).first()
    db.delete(capy)
    db.commit()
    return None 
