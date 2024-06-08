
## AutoAIResponder

This script uses Ollama Python module to interact with a chatbot, and help write messages for you.

### How it works.
- You Copy a message you want to respond too
- Put your cursor in the response box.
- Type '\'
- The Script will respond to your copied message
- The \ will be deleted and the response pasted and Enter pressed.
- The script keeps a running context of the past 20 messages, which can be reset with by pressing '='
- To exit the script press 'esc'

### How to run

Required python packages: pyperclip, ollama, keyboard
Reqired programs: Ollama, and a AI model of your choosing with a set system prompt.

1. The first step is to make a custom model in Ollama with a system prompt such as:

  *You are name who is a [], you like []ect.., respond to incomming messages. Keep your responses short (under 10 words), punctuation is unessesary.*

2. Start up Ollama and run the script.
