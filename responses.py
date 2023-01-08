import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "hola":
        return "Hola , Como estas? 😊"

    if message == "roll":
        return str(random.randint(1, 6))

    if p_message == "!help":
        return "`in which way can I help you?`"  

    return "I did not understand what you wrote"          