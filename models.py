from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password_hash = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

class Route(Base):
    __tablename__ = "routes"
    route_id = Column(Integer, primary_key=True, index=True)
    origin = Column(String(255))
    destination = Column(String(255))
    distance_km = Column(Float)
    estimated_time = Column(Float)
    cost = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

class TransportMode(Base):
    __tablename__ = "transport_modes"
    mode_id = Column(Integer, primary_key=True, index=True)
    mode_name = Column(String(255))
    avg_speed = Column(Float)
    cost_per_km = Column(Float)

class AIPrediction(Base):
    __tablename__ = "ai_predictions"
    prediction_id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("routes.route_id"))
    recommended_mode = Column(Integer, ForeignKey("transport_modes.mode_id"))
    predicted_cost = Column(Float)
    predicted_time = Column(Float)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
