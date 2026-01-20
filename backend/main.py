from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.signup import router as signup_router

app = FastAPI(title="Signup API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 如果部署可以改成前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(signup_router)