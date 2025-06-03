import tkinter as tk
from tkinter import scrolledtext
import datetime
import re
import random

# Portfolio data
portfolio_data = {
    "name": "Muhammad Fahad",
    "title": "Frontend Developer | Advancing in MERN Stack",
    "education": "B.Sc. Computer Science\nIslamia University Bahawalpur",
    "experience": "1 Year\nFrontend Development",
    "projects": "30+ Practice Projects",
    "learning": "Backend Development (Beginner)",
    "skills": ["React", "JavaScript", "HTML", "CSS", "Tailwind", "Git", "Responsive Design"],
    "testimonials": [
        {
            "name": "Hassan Raza",
            "position": "CEO Bytelogist",
            "testimonial": "Fahad is a true professional. Their attention to detail and commitment to quality are unmatched. They were always responsive and willing to go the extra mile to ensure our satisfaction. We highly recommend their services."
        },
        {
            "name": "Ayesha Shoaib",
            "position": "HR at Evionics",
            "testimonial": "Fahad demonstrates a deep understanding of modern web development frameworks and tools. His sites are responsive, user-friendly, and aesthetically pleasing. Whether custom-built or integrating third-party services, his versatility shines through."
        }
    ],
    "certifications": [
        "React Basics", "Git & Github", "Responsive Web Design", "Exploratory Data Analysis In Python"
    ],
    "contact": "Feel free to reach out to me on any of the following platforms.\nI look forward to connecting with you!"
}

# Pattern-response pairs
pairs = [
    [r"(.*)(your name|who are you)(.*)", [f"My name is {portfolio_data['name']}"]],
    [r"(.*)(title|position|role)(.*)", [f"I am a {portfolio_data['title']}"]],
    [r"(.*)(education|study|university|degree)(.*)", [f"My education:\n{portfolio_data['education']}"]],
    [r"(.*)(experience|work|job)(.*)", [f"My experience:\n{portfolio_data['experience']}"]],
    [r"(.*)(project)(.*)", [f"I have worked on {portfolio_data['projects']}"]],
    [r"(.*)(learning|currently learning|studying)(.*)", [f"I am currently learning {portfolio_data['learning']}"]],
    [r"(.*)(skill|technologies|tools)(.*)", [f"My skills include: {', '.join(portfolio_data['skills'])}"]],
    [r"(.*)(testimonial|feedback|review)(.*)", [
        "\n\n".join(
            f"{t['name']} ({t['position']}):\n\"{t['testimonial']}\"" for t in portfolio_data['testimonials']
        )
    ]],
    [r"(.*)(certification|certificate|courses)(.*)", [
        f"My certifications include: {', '.join(portfolio_data['certifications'])}"
    ]],
    [r"(.*)(contact|connect|reach)(.*)", [portfolio_data['contact']]],
    [r"(.*)help(.*)", [
        "You can ask me about:\n"
        "- My name\n"
        "- My title or experience\n"
        "- My skills or projects\n"
        "- My testimonials or certifications\n"
        "- How to contact me"
    ]],
    [r"(.*)", ["I'm not sure I understand. Try asking about my skills, projects, or education."]]
]

# Get response using regex pairs
def get_response(user_input):
    for pattern, responses in pairs:
        if re.match(pattern, user_input.lower()):
            return random.choice(responses)
    return "I'm not sure I understand. Can you rephrase?"

# Tkinter setup
window = tk.Tk()
window.title("Muhammad Fahad's Portfolio Chatbot")
window.geometry("600x500")
window.resizable(False, False)

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled', font=("Arial", 12), bg="#f9f9f9")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

user_input = tk.Text(window, height=2, font=("Arial", 12))
user_input.pack(padx=10, pady=(0, 10), side=tk.LEFT, fill=tk.X, expand=True)

def send_message(event=None):
    message = user_input.get("1.0", tk.END).strip()
    if message == "":
        return
    timestamp = datetime.datetime.now().strftime("%H:%M")
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, f"[{timestamp}] You: {message}\n")
    response = get_response(message)
    chat_area.insert(tk.END, f"[{timestamp}] Bot:\n{response}\n{'-'*60}\n")
    chat_area.configure(state='disabled')
    chat_area.yview(tk.END)
    user_input.delete("1.0", tk.END)

def clear_chat():
    chat_area.configure(state='normal')
    chat_area.delete(1.0, tk.END)
    chat_area.configure(state='disabled')

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(padx=10, pady=(0, 10), side=tk.RIGHT)

clear_button = tk.Button(window, text="Clear", command=clear_chat)
clear_button.pack(padx=10, pady=(0, 10), side=tk.RIGHT)

chat_area.configure(state='normal')
chat_area.insert(tk.END, "Bot: Hi there! I'm your portfolio assistant. Ask me anything about Fahad's profile.\n" + "-"*60 + "\n")
chat_area.configure(state='disabled')

user_input.bind("<Return>", send_message)

window.mainloop()
