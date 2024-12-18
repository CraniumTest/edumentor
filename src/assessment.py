import random

class Assessment:
    def __init__(self, topic: str):
        self.topic = topic
        self.questions = self.load_questions()

    def load_questions(self):
        # In a real scenario, load from database or external source
        return [
            {"question": "What is Python?", "difficulty": "easy"},
            {"question": "Explain inheritance in OOP.", "difficulty": "medium"},
            {"question": "Discuss the time complexity of QuickSort.", "difficulty": "hard"},
        ]

    def present_question(self):
        question = random.choice(self.questions)
        return question["question"]
