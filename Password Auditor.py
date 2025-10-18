from tkinter import messagebox
import customtkinter as ctk
import re
import random
import string
import hashlib

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password toughness Auditor")
app.geometry("500x450")

def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()

def suggest_password(password):
    suggestions = []
    if not re.search(r"[A-Z]", password):
        suggestions.append(random.choice(string.ascii_uppercase))
    if not re.search(r"[a-z]", password):
        suggestions.append(random.choice(string.ascii_lowercase))
    if not re.search(r"[0-9]", password):
        suggestions.append(random.choice(string.digits))
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append(random.choice("!@#$%^&*()"))
    while len(password) + len(suggestions) < 8:
        suggestions.append(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()"))
    return password + ''.join(suggestions)

def check_password():
    password = password_entry.get()
    strength = 0

    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    progress_bar.set(strength / 6)
    
    if strength <= 2:
        result_label.configure(text="Weak Password", text_color="red")
        suggestion = suggest_password(password)
        suggestion_label.configure(text=f"Suggestion: {suggestion}")
    elif strength <= 4:
        result_label.configure(text="Neutral Password", text_color="orange")
        suggestion_label.configure(text="Try adding symbols or numbers to improve strength")
    elif strength <= 5:
        result_label.configure(text="Strong Password", text_color="green")
        suggestion_label.configure(text="")
    else:
        result_label.configure(text="Brilliant Password", text_color="blue")
        suggestion_label.configure(text="")

    if save_var.get():
        hashed = hash_password(password)
        with open("passwords.txt", "a") as file:
            file.write(hashed + "\n")
        messagebox.showinfo("Saved", "Password saved securely!")

def toggle_password():
    if password_entry.cget('show') == "*":
        password_entry.configure(show="")
        eye_button.configure(text="👁")
    else:
        password_entry.configure(show="*")
        eye_button.configure(text="⌣")

title_label = ctk.CTkLabel(app, text="Password Toughness Auditor", font=("Segoe UI", 22, "bold"))
title_label.pack(pady=(20, 5))

subtitle_label = ctk.CTkLabel(app, text="Create a secure password 🔐", font=("Segoe UI", 14))
subtitle_label.pack(pady=(0, 15))

main_frame = ctk.CTkFrame(app, corner_radius=15)
main_frame.pack(padx=20, pady=10, fill="both", expand=True)

entry_container = ctk.CTkFrame(main_frame, fg_color="transparent")
entry_container.pack(pady=20, padx=20, fill="x")

password_entry = ctk.CTkEntry(
    entry_container,
    placeholder_text="Enter Password",
    show="*",
    height=40,
    font=("Segoe UI", 14)
)
password_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
eye_button = ctk.CTkButton(
    entry_container,
    text="👁",
    width=40,
    height=36,
    fg_color="transparent",
    hover_color=("#2b2b2b", "#727999"),
    command=toggle_password
)
eye_button.pack(side="right", padx=(0, 0))
save_var = ctk.BooleanVar()
save_checkbox = ctk.CTkCheckBox(main_frame, text="Save Password Securely", variable=save_var)
save_checkbox.pack()

progress_bar = ctk.CTkProgressBar(main_frame, width=350)
progress_bar.set(0)
progress_bar.pack(pady=10)

result_label = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 14, "bold"))
result_label.pack(pady=5)

suggestion_label = ctk.CTkLabel(main_frame, text="", text_color="lightblue", justify="left")
suggestion_label.pack(pady=5)

check_button = ctk.CTkButton(main_frame, text="Check Strength", height=35, command=check_password)
check_button.pack(pady=15)


app.mainloop()
