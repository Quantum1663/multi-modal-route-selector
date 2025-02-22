from database import engine, Base

# Create tables in database
Base.metadata.create_all(bind=engine)
print("✅ Database tables created successfully!")
