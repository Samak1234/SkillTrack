from app.database import engine

try:
    with engine.connect() as connection:
        print("SkillTrack database connected successfully!")
except Exception as error:
    print("Database connection failed:")
    print(error)