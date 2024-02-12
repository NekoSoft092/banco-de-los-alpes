import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app_version: str = 'v1'
app_prefix: str = '/api/'+app_version+'/es'

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
        # access to frontend apps
        "http://localhost:1420",
        "http://localhost:5500",
        "http://localhost",
        "http://127.0.0.1:1420",
        "http://127.0.0.1:5500",
        "https://example.com",
        "https://www.example.com",
        "https://api.example.com",
        "https://app.example.com",
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
)

# Application health  
@app.get("/status")
async def check_status():
    return {"status": "available"}

# Hello world
@app.get("/")
async def home():
    return {"message": "Hello World!!! "}

# Run uvicorn script  
if __name__ == '__main__':
    port_env: int= int(7878)
    uvicorn.run("main:app", port=port_env, reload=True)
