from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models import Config
from schemas import ConfigBase

router = APIRouter()

@router.get("/config", response_model=List[ConfigBase])
async def get_config(db: Session = Depends(get_db)):
    """Fetches all config records."""
    try:
        results = db.query(Config).filter(Config.is_deleted == False).all()
        if not results:
            raise HTTPException(status_code=404, detail="No config data found")
        return results
    except Exception as e:
        print(f"Error fetching config data: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch config data")
