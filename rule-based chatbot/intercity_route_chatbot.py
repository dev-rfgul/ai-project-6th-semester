import tkinter as tk
from tkinter import ttk, messagebox

# Route definitions
city_routes = {
    ("bahawalpur", "multan"): "Take N-5 National Highway or M-5 Motorway (approx. 1.5 hours).",
    ("multan", "lahore"): "Use M-4 Motorway → M-3 → M-2 towards Lahore (approx. 4 hours).",
    ("lahore", "islamabad"): "Take M-2 Motorway via Sheikhupura & Kallar Kahar (approx. 4.5 hours).",
    ("bahawalpur", "lahore"): "Take N-5 via Multan → Khanewal → Lahore (approx. 6 hours).",
    ("lahore", "faisalabad"): "Via M-3 Motorway (approx. 2 hours).",
    ("faisalabad", "islamabad"): "Take M-4 → M-2 Motorway (approx. 4.5 hours).",
    ("sialkot", "lahore"): "Use Lahore-Sialkot Motorway (approx. 1.5 hours).",
    ("islamabad", "murree"): "Via Murree Expressway (approx. 1.5 hours).",
    ("multan", "faisalabad"): "Via M-4 Motorway (approx. 3 hours)."
}

# Unique list of cities
cities = sorted(set([city for route in city_routes.keys() for city in route]))

def find_route():
    start = source_var.get().strip().lower()
    end = dest_var.get().strip().lower()

    if start == "" or end == "":
        messagebox.showwarning("Missing Info", "Please select both starting and destination cities.")
        return

    if start == end:
        result.set("You are already in the destination city.")
        return

    key = (start, end)
    if key in city_routes:
        result.set(f"Route from {start.title()} to {end.title()}:\n{city_routes[key]}")
    else:
        result.set("Sorry, no direct route found between these cities.")

# GUI setup
root = tk.Tk()
root.title("🛣️ Intercity Route Chatbot (Dropdown Version)")
root.geometry("550x330")
root.resizable(False, False)

tk.Label(root, text="Intercity Route Chatbot", font=("Helvetica", 16, "bold")).pack(pady=10)

# Starting City Dropdown
tk.Label(root, text="Starting City:").pack()
source_var = tk.StringVar()
source_menu = ttk.Combobox(root, textvariable=source_var, values=cities, state="readonly", width=35)
source_menu.pack(pady=5)

# Destination City Dropdown
tk.Label(root, text="Destination City:").pack()
dest_var = tk.StringVar()
dest_menu = ttk.Combobox(root, textvariable=dest_var, values=cities, state="readonly", width=35)
dest_menu.pack(pady=5)

# Result display (now in black color)
result = tk.StringVar()
tk.Label(root, textvariable=result, wraplength=500, justify="left", font=("Arial", 11), fg="black").pack(pady=15)

# Find Route button
tk.Button(root, text="Find Route", command=find_route, bg="green", fg="white", width=15).pack()

root.mainloop()
