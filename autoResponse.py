import keyboard
import pyperclip
import time
import ollama

model_name = 'llama-daniel'
messages = []
context_length = 20

def respond():
    global messages
    try:
        # Get clipboard content
        content = pyperclip.paste()
        print("user:" + content)
        print("Current Context Length: " + str(len(messages)))

        # Save to messages
        messages.append({'role': 'user', 'content': content})
        response = ollama.chat(model=model_name, messages=messages)
        bot_response = response['message']['content']
        print(f"Bot: {bot_response}")
        messages.append({'role': 'assistant', 'content': bot_response})
        messages = messages[-context_length:]
        send_message(bot_response)

    except Exception as e:
        print(f"Error accessing clipboard: {e}")

def send_message(message):
     # Copy the message to the clipboard
    pyperclip.copy(message)

    keyboard.press_and_release('ctrl+a')
    time.sleep(0.1)  # Small delay to ensure the operation completes
    keyboard.press_and_release('backspace')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+v')
    time.sleep(0.1)
    keyboard.press_and_release('enter')
    time.sleep(0.1)


def clear_list():
    global messages
    messages.clear()
    print("message history cleared.")

def main():
    # Define the key event handlers
    keyboard.add_hotkey('\\', respond)
    keyboard.add_hotkey('=', clear_list)
    
    print("Press '\\' to respond.")
    print("Press '=' to clear the message history.")
    print("Press 'esc' to exit.")

    # Keep the script running
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
