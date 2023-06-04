import uvicorn
from routers.capys import query

from fastapi import FastAPI

app = FastAPI(
    title='Capy API',
    description="Данное API позволяет взаимодействовать с библиотекой капибар",
    version='1.0.0',
    contact={
            "name": "Шохин Е.П.\nФИТ-221",
            "email": "djegor2004@gmail.com",
        },
)
app.include_router(query.router)

if __name__ == '__main__':
    uvicorn.run(app)