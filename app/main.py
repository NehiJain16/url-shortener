from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import time

from app import redis_client

from .database import SessionLocal, engine
from .models import Base, URL
from .schemas import URLCreate, URLResponse
from .utils import encode_base62

# -----------------------------
# App initialization
# -----------------------------
app = FastAPI(title="URL Shortener Service")

# Create DB tables
Base.metadata.create_all(bind=engine)

# -----------------------------
# Database dependency
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -----------------------------
# Simple in-memory rate limiter
# -----------------------------
RATE_LIMIT = 5
TIME_WINDOW = 60

def check_rate_limit(ip: str):
    key = f"rate_limit:{ip}"
    current_count = redis_client.get(key)

    if current_count is None:
        redis_client.setex(key, TIME_WINDOW, 1)
        return True

    if int(current_count) >= RATE_LIMIT:
        return False

    redis_client.incr(key)
    return True

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def health_check():
    return {"status": "URL Shortener is running"}

# -----------------------------
# Create short URL
# -----------------------------
@app.post("/shorten", response_model=URLResponse)
def create_short_url(
    data: URLCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    ip = request.client.host

    if not check_rate_limit(ip):
        raise HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )

    # Save original URL first
    new_url = URL(original_url=data.original_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    # Generate Base62 short code using DB id
    short_code = encode_base62(new_url.id)
    new_url.short_code = short_code
    db.commit()

    return {
    "short_url": f"{request.base_url}{short_code}"
    }

# -----------------------------
# Redirect short URL
# -----------------------------
@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url.original_url)

# -----------------------------
# Delete short URL
# -----------------------------
@app.delete("/{short_code}")
def delete_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    db.delete(url)
    db.commit()

    return {"message": "Short URL deleted successfully"}
