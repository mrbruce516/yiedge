from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from backend.db.db import SessionLocal
from backend.db.check import SignupForm
from backend.db.model import Signup

router = APIRouter()

# 数据库依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
async def submit_form(form: SignupForm, db: Session = Depends(get_db)):
    # 重复检查
    existing = db.query(Signup).filter(Signup.email == form.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="すでにメールで登録済みです。")

    # 写入数据库
    signup_entry = Signup(
        name=form.name,
        email=form.email,
        phone=form.phone
    )
    db.add(signup_entry)
    db.commit()
    db.refresh(signup_entry)

    return {"message": "登録が完了しました！", "id": signup_entry.id}