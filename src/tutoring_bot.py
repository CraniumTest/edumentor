from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class TutoringBot:
    def __init__(self):
        self.model_name = "gpt2"
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)

    def get_response(self, query: str):
        inputs = self.tokenizer.encode(query, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=150, num_return_sequences=1)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

# Usage example:
# tutor = TutoringBot()
# response = tutor.get_response("Explain Newton's Laws of Motion")
# print(response)
