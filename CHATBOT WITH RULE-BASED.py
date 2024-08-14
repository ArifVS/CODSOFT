def chatbot_response(user_input):
    # Convert input to lowercase for uniformity
    user_input = user_input.lower()
    
    # Define responses based on keywords
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am a chatbot created to help you with basic questions."
    elif "how are you" in user_input:
        return "I'm just a program, but I'm here and ready to assist you!"
    elif "thank you" in user_input:
        return "You're welcome! If you have any more questions, feel free to ask."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

def main():
    print("Welcome to the chatbot! Type 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
