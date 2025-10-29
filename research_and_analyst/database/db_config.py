from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from passlib.context import CryptContext

# Password hashing context(bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

DATABASE_URL = "sqlite:///./users.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

# Create DB tables
Base.metadata.create_all(bind=engine)

def hash_password(password: str) -> str:
    safe_pw = password[:50]
    return pwd_context.hash(safe_pw)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    safe_pw = plain_password[:50]
    return pwd_context.verify(safe_pw, hashed_password)