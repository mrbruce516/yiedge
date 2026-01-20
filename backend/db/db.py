from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = "mysql+pymysql://root:zc990516@localhost/yiedge"

engine = create_engine(db)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)