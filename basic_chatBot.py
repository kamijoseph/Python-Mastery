
#This a very simple chatbot
def chatBot(user_input):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm just a program, but I'm here to help you! How about you?",
        "what is your name": "I'm your friendly chatbot! What's yours?",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm not sure how to respond to that. Could you ask something else?"
    }
    
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])