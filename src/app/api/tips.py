from fastapi import APIRouter, HTTPException, Depends
from typing import List
from ..models.tip import Tip
from ..database.database import get_db_connection, init_db
import random

def get_router():
    router = APIRouter()
    
    @router.on_event("startup")
    def startup():
        init_db()
    
    @router.post("/tips", response_model=Tip)
    def create_tip(tip: Tip):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tips (text) VALUES (?)',
            (tip.text,)
        )
        tip_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return {**tip.dict(), "id": tip_id}
    
    @router.get("/tips/random", response_model=Tip)
    def get_random_tip():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, text FROM tips')
        tips = cursor.fetchall()
        conn.close()
        
        if not tips:
            raise HTTPException(status_code=404, detail="No tips found")
        
        tip = random.choice(tips)
        return dict(tip)
    
    return router