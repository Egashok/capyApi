from pydantic import BaseModel

class CapyBase(BaseModel):
    name:str
    description:str
    photo:str

class CapyToCreate(CapyBase):
    pass

class Capy(CapyBase):
    id: int
    class Config:
        orm_mode = True
