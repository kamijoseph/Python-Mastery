
#This a very simple chatbot
#Stupid but fine

def chatBot(user_input):
    responses = {
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm just a program, but I'm here to help you! How about you?",
        "what is your name": "I'm your friendly chatbot Fate! What's yours?",
        "bye": "Goodbye! Have a great day!",
        "fine": "That is good to hear",
        "default": "I'm not sure how to respond to that. Could you ask something else?"
    }
    
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

def main():
    bot = "Fate"
    print(f"Welcome to the chat bot. My name is {bot}")
    user_name = input("What is Your Name: ")
    print(f"Nice name {user_name}")
    
    while True:
        user_input = input(f"{user_name}: ").lower()
        if user_input == "bye":
            print(f"{bot}: Goodbye! Have a Great day!")
            break
        rensponse = chatBot(user_input)
        print(f"{bot}: {rensponse}")
        
if __name__ == "__main__":
    main()