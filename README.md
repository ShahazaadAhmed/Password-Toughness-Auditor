# Password Toughness Auditor

## Description

The **Password Toughness Auditor** is a GUI-based Python application built using **CustomTkinter**. It helps users evaluate the strength of their passwords, provides real-time feedback on password quality, and suggests improvements to enhance security. Additionally, users can securely hash and save passwords locally for reference.

## Features

* **Modern GUI**: Designed using CustomTkinter with a dark theme for a smooth, user-friendly experience.
* **Password Strength Analysis**: Evaluates passwords based on length, character variety, and symbol inclusion.
* **Real-Time Suggestions**: Provides instant feedback and improvement tips.
* **Password Hashing**: Uses SHA-512 hashing to securely save passwords.
* **Visibility Toggle**: Show or hide password input using an eye button.
* **Progress Bar Indicator**: Visually represents password strength.
* **Secure Save Option**: Option to securely store hashed passwords in a local file.

## Requirements

Before running the application, make sure you have:

* **Python 3.8+** installed
* **CustomTkinter** library for GUI

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/password-toughness-auditor.git
   cd password-toughness-auditor
   ```

2. **Install Dependencies**:

   ```bash
   pip install customtkinter
   ```

## Usage

### Running the Application

Run the following command to start the program:

```bash
python passchek.py
```

Or, if using the standalone version:

```bash
password_auditor.exe
```

### Checking Password Strength

1. Enter your password in the input field.
2. Click **Check Strength**.
3. The progress bar and text indicators will show your password strength (Weak, Neutral, Strong, Brilliant).
4. If your password is weak, the app will suggest improvements.

### Saving Passwords

1. Check the **Save Password Securely** option.
2. Click **Check Strength**.
3. Your password will be hashed using **SHA-512** and saved in a file named `passwords.txt`.

### Show or Hide Password

Click the **👁 (eye)** icon to toggle password visibility.

### Troubleshooting

If you face any errors or crashes:

1. **Extract the ZIP file** (if provided).
2. Locate and run the **password_auditor.exe** file.
3. Follow the same password checking steps as above.

## Project Structure

```
.
├── passchek.py        # Main application script
├── README.md          # Project documentation
├── passwords.txt      # File where hashed passwords are saved
```

## How It Works

1. The app checks your password length, uppercase, lowercase, digits, and special characters.
2. A score (0–6) determines your password’s strength.
3. The result is shown visually via a progress bar and text message.
4. If enabled, the password is hashed and saved securely.

## License

This project is licensed under the **MIT License**.

## Contribution

Contributions are welcome! If you have ideas for improvement or new features, feel free to fork the repository and create a pull request.
