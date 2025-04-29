import torch
from transformers import GPT2LMHeadModel

class ChatBot:
    def __init__(self, model_name="gpt2"):
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
    
    def generate_response(self, input_text, tokenizer):
        input_ids = tokenizer.encode(input_text, return_tensors="pt")
        response = self.model.generate(input_ids, max_length=50)
        return tokenizer.decode(response[0], skip_special_tokens=True)