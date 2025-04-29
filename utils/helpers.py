import json

def save_chat_history(message):
    """Save messages to a JSON file for training."""
    with open("data/chat_history.json", "a") as file:
        json.dump({"author": str(message.author), "content": message.content}, file)
        file.write("\n")