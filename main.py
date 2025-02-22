from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Route, AIPrediction

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API to fetch all routes
@app.get("/routes/")
def get_routes(db: Session = Depends(get_db)):
    return db.query(Route).all()

# API to get AI prediction for a route
@app.get("/predict/{route_id}")
def get_prediction(route_id: int, db: Session = Depends(get_db)):
    prediction = db.query(AIPrediction).filter(AIPrediction.route_id == route_id).first()
    return prediction if prediction else {"message": "No prediction found"}
