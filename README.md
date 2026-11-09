# Basic Rule-Based Chatbot 🤖

A simple console chatbot written in Python that replies to a few predefined messages using `if-elif` rules.

## Features
- Replies to greetings, "how are you", name questions, thanks and goodbyes
- Not case-sensitive and ignores punctuation (`Hello!` works the same as `hello`)
- Keeps chatting in a loop until you say goodbye
- Friendly fallback reply for anything it doesn't understand

## Concepts Used
`if-elif` · functions · `while` loop · input/output

## How to Run
1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repository or download `chatbot.py`
3. Run in a terminal:
   ```bash
   python chatbot.py
   ```

## Sample Conversation
```
You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: bye
Bot: Goodbye!
```

## Supported Messages
| You say | Bot replies |
|---|---|
| hello / hi / hey | Hi! |
| how are you | I'm fine, thanks! |
| what is your name | I'm a simple rule-based chatbot. |
| thanks / thank you | You're welcome! |
| help | Lists what you can say |
| bye / goodbye / exit / quit | Goodbye! (ends the chat) |
