import tkinter as tk
from tkinter import scrolledtext

# Rule-based weather data
weather_data = {
    "bahawalpur": {
        "today": "Sunny with a high of 40°C and low of 27°C.",
        "tomorrow": "Partly cloudy with a high of 38°C and low of 26°C."
    },
    "lahore": {
        "today": "Cloudy with a high of 35°C and chances of rain.",
        "tomorrow": "Rain expected, high of 33°C and low of 24°C."
    },
    "karachi": {
        "today": "Humid and warm, high of 34°C, low of 29°C.",
        "tomorrow": "Hot and dry, high of 36°C, low of 30°C."
    }
}

# Chatbot logic
def get_weather_response(user_input):
    user_input = user_input.lower()
    for city in weather_data:
        if city in user_input:
            if "today" in user_input:
                return f"Weather in {city.title()} today: {weather_data[city]['today']}"
            elif "tomorrow" in user_input:
                return f"Weather in {city.title()} tomorrow: {weather_data[city]['tomorrow']}"
            else:
                return f"Please ask about 'today' or 'tomorrow' weather in {city.title()}."
    return "Sorry, I don't have weather info for that location."

# GUI setup
def send():
    user_msg = entry.get()
    if user_msg:
        chat_window.insert(tk.END, "You: " + user_msg + "\n")
        bot_response = get_weather_response(user_msg)
        chat_window.insert(tk.END, "Bot: " + bot_response + "\n\n")
        entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("☁️ Weather Chatbot")
root.geometry("450x500")
root.resizable(False, False)

# Chat window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 11))
chat_window.pack(pady=10)
chat_window.insert(tk.END, "Bot: Hello! Ask me the weather in Bahawalpur, Lahore, or Karachi (e.g. 'weather in Lahore today')\n\n")

# Input
entry = tk.Entry(root, width=45, font=("Arial", 12))
entry.pack(pady=5)

# Send button
send_btn = tk.Button(root, text="Send", width=10, command=send)
send_btn.pack(pady=5)

root.mainloop()
