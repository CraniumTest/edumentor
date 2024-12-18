from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Dummy in-memory database for user profiles
user_profiles = {}

# Pydantic model for user registration
class User(BaseModel):
    username: str
    level: str

@app.post("/register/")
def register_user(user: User):
    user_profiles[user.username] = {"level": user.level, "progress": {}}
    return {"message": f"User {user.username} registered successfully"}

@app.get("/tutor/{username}/{query}")
def tutor_help(username: str, query: str):
    # Initialize a language model pipeline
    conversational_agent = pipeline("conversational")
    response = conversational_agent(query)
    return {"response": response}

@app.get("/progress/{username}")
def get_progress(username: str):
    profile = user_profiles.get(username)
    if not profile:
        return {"error": "User not found"}
    return {"progress": profile["progress"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
