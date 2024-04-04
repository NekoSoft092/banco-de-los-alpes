import os
from dotenv import load_dotenv
load_dotenv()

from utils.logs import printLog

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import get_db
from sqlalchemy.orm import Session

from routes.auth_route import router as router_auth
from routes.card_routes import router as router_cards
from routes.request_routes import router as router_request

routers = [
    router_auth,
    router_cards,
    router_request
]

app: FastAPI = FastAPI(
    title='alpes-bank', 
    description='alpes bank project to implements credit cards system', 
    version='0.0.1',
    docs_url='/v1/openapi.json',
    openapi_url='/v1/openapi.json',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

# routes
for router in routers:
    app.include_router(router)



# Application health  
@app.get("/status")
async def check_status():
    return {"status": "available"}

# Hello world
@app.get("/")
async def home():
    return {"message": "Hello World!!! "}

@app.get("/test-db", status_code=200)
async def test_database(db: Session= Depends(get_db)):
    return {"message": "server is connected"}

# Run uvicorn script  
if __name__ == '__main__':

    if os.getenv('PORT') != None:
        port_env: int = int( os.getenv('PORT'))
        uvicorn.run("main:app", port=port_env, reload=True)
    else:
        printLog('Port is not configured')
