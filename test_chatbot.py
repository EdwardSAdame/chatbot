from app import SimpleChatbot

def test_chatbot_responses():
    """
    Test the chatbot's responses to a set of predefined inputs.
    """
    # Initialize the chatbot
    bot = SimpleChatbot()

    # Define test inputs and expected behavior
    test_inputs = [
        "Hello!",
        "What's your name?",
        "Tell me a joke.",
        "How's the weather?",
        "Goodbye!"
    ]

    # Test each input and print responses
    for user_input in test_inputs:
        print(f"User: {user_input}")
        response = bot.get_response(user_input)
        assert response, f"Response to '{user_input}' was empty!"
        print(f"Chatbot: {response}")
        print("-" * 30)

# Run the tests
if __name__ == "__main__":
    test_chatbot_responses()

