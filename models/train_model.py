import torch
import json
from chatbot_model import ChatBot
from transformers import GPT2Tokenizer
import config

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = ChatBot()

optimizer = torch.optim.Adam(model.model.parameters(), lr=config.LEARNING_RATE)
criterion = torch.nn.CrossEntropyLoss()

chat_data = []
with open("data/chat_history.json", "r") as file:
    for line in file:
        msg = json.loads(line)
        chat_data.append(tokenizer.encode(msg["content"], return_tensors="pt"))

for epoch in range(config.EPOCHS):
    for text_tensor in chat_data:
        outputs = model.model(text_tensor, labels=text_tensor)
        loss = criterion(outputs.logits.view(-1, model.model.config.vocab_size), text_tensor.view(-1))
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch} Loss: {loss.item()}")

# Save model after training
model.model.save_pretrained("models/trained_chatbot")
tokenizer.save_pretrained("models/trained_chatbot")