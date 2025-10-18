# Password Toughness Auditor

A simple yet effective password strength checker and auditor built with Python using the `Tkinter` and `customTkinter` libraries. This tool helps you assess the strength of your passwords, suggests improvements, and allows you to save them securely by hashing.

## Features

- **Password Strength Checker**: Assesses password strength based on length, use of uppercase, lowercase, digits, and special characters.
- **Password Suggestions**: If the password is weak, the tool suggests improvements (e.g., adding uppercase letters, numbers, or symbols).
- **Visual Progress Bar**: Provides a visual indicator of password strength.
- **Secure Password Saving**: Option to save hashed passwords securely to a file.
- **Password Visibility Toggle**: Easily show or hide your password while typing.

## Requirements

- Python 3.x
- `customtkinter` (for the GUI)
- `hashlib` (for password hashing)
- `re` (for regular expression-based password strength checks)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/password-toughness-auditor.git
2. Install the required dependencies:
   ```bash

   How to Use

Enter a Password: Type your password into the input field.

Check Strength: Click the "Check Strength" button to assess the strength of your password.

View Suggestions: If your password is weak, suggestions for improvement will appear.

Save Password: Optionally, you can choose to save your password (hashed) securely by checking the "Save Password Securely" checkbox.

Password Strength Criteria

Weak Password: A password that fails to meet the basic security requirements (e.g., minimum length or missing key character types).

Neutral Password: A password that meets some but not all criteria for strong passwords.

Strong Password: A password that is sufficiently complex and meets most security standards.

Brilliant Password: A password that is considered highly secure, meeting all best practices.

File Storage

Passwords are saved as SHA-512 hashes in a text file (passwords.txt) for security.

#Contributing

Feel free to open an issue or create a pull request if you want to contribute improvements or fixes to this project.
   
