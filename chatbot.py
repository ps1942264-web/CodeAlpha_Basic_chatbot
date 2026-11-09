"""
Task 2: Basic Rule-Based Chatbot
--------------------------------
A simple console chatbot that replies to a few predefined messages.

Example:
    You: hello          ->  Bot: Hi!
    You: how are you    ->  Bot: I'm fine, thanks!
    You: bye            ->  Bot: Goodbye!

Concepts used: if-elif, functions, loops, input/output.
"""

# Words that end the conversation
GOODBYE_WORDS = ["bye", "goodbye", "exit", "quit"]


def clean_input(text):
    """Make the input easy to compare: lowercase, no extra spaces or punctuation."""
    return text.lower().strip(" ?!.,")


def get_response(message):
    """Return the chatbot's reply for a cleaned-up user message."""
    if message in ["hello", "hi", "hey"]:
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message in ["what is your name", "who are you", "your name"]:
        return "I'm a simple rule-based chatbot."
    elif message in ["thanks", "thank you"]:
        return "You're welcome!"
    elif message == "help":
        return "Try saying: hello, how are you, what is your name, thanks, or bye."
    elif message in GOODBYE_WORDS:
        return "Goodbye!"
    elif message == "":
        return "Please type something."
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can reply to."


def run_chatbot():
    """Keep chatting until the user says goodbye."""
    print("==============================")
    print("        SIMPLE CHATBOT")
    print("==============================")
    print("Say 'hello', 'how are you' or 'bye'. Type 'help' for more.\n")

    while True:
        user_message = clean_input(input("You: "))
        reply = get_response(user_message)
        print("Bot:", reply)

        if user_message in GOODBYE_WORDS:
            break  # end the loop (and the chat)


if __name__ == "__main__":
    run_chatbot()
