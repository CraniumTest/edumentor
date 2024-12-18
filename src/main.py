from fastapi import FastAPI
from src.learning_path import LearningPath
from src.tutoring_bot import TutoringBot
from src.assessment import Assessment

app = FastAPI()

@app.get("/learning-path/{student_id}")
def get_learning_path(student_id: int):
    path = LearningPath(student_id)
    return {"path": path.generate_path()}

@app.get("/ask")
def ask(question: str):
    tutor = TutoringBot()
    response = tutor.get_response(question)
    return {"response": response}

@app.get("/assessment/{topic}")
def assessment(topic: str):
    assess = Assessment(topic)
    question = assess.present_question()
    return {"question": question}
