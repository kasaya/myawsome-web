# -*- coding: utf-8 -*-
# main.py
# @Author ouyang
# @Description  
# @Created  2022-01-10T14:15:40.589Z+08:00
# @Modified  2022-01-10T14:57:26.238Z+08:00
#
from fastapi import FastAPI
from app.excetpion.customer_exception import AppcationExcetpion
import app.routers.router as myrouter
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.types import Message
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


def create_app():
    app = FastAPI()
    app.include_router(myrouter.apiRouter, prefix='/api')
    app.exception_handlers
    return app

app = create_app()


if __name__ == '__main__':
    uvicorn.run(app='app.main:app', host='127.0.0.1', port=8000, reload=True)


@app.exception_handler(AppcationExcetpion)
async def application_excetpion_handler(request:Request, exc: AppcationExcetpion):
    return JSONResponse(
        status_code=418,
        content={
            'errorCode':exc.err_code,
            'message':exc.err_message
            }
    )

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)