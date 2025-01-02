
#This a very simple chatbot
def chatBot(user_input):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm just a program, but I'm here to help you! How about you?",
        "what is your name": "I'm your friendly chatbot Fate! What's yours?",
        "bye": "Goodbye! Have a great day!",
        "default": "I'm not sure how to respond to that. Could you ask something else?"
    }
    
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

def main():
    bot = "Fate"
    user_name = input("Enter Your Name: ")
    print(f"Welcome to the chat bot {user_name}. My name is {bot}")
    
    while True:
        user_input = input(f"{user_name}: ").lower()
        if user_input == "bye":
            print(f"{bot}: Goodbye! Have a Great day!")
            break
        rensponse = chatBot(user_input)
        print(f"{bot}: {rensponse}")
        
if __name__ == "__main__":
    main()