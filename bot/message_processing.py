import nltk
from transformers import GPT2Tokenizer

nltk.download("punkt")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def preprocess_text(text):
    return tokenizer.encode(text, return_tensors="pt")