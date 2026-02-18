📝 Personal Journal Manager
<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Project Status">
<img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Platform">
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

📖 Table of Contents
Overview

Features

Screenshot Demo

Project Architecture

How to Run

Concepts Demonstrated

Future Improvements

License

🚀 Overview
Personal Journal Manager is a professional-grade Command Line Interface (CLI) application designed for efficient daily reflection and note-taking. It provides a secure and persistent way to store personal thoughts locally using a flat-file database system, ensuring your data remains private and accessible.

✨ Features
Persistent Storage: Automatically creates and manages a journal.txt file to save your entries forever.

Intuitive Search: Quickly locate past reflections using keyword-based searching.

Full CRUD Support: Add, View, Search, and Delete operations for complete control over your data.

Input Validation: Robust handling of user menu selections to prevent crashes.

🖥️ Screenshot Demo
<details>
<summary><b>1. Main Menu Interface</b></summary>



The clean, numbered menu system allows for easy navigation between features.



<img src="unnamed.png" alt="Main Menu">
</details>

<details>
<summary><b>2. Adding a New Entry</b></summary>



Simple prompt-based entry system with immediate success confirmation.



<img src="unnamed(1).png" alt="Add Entry">
</details>

<details>
<summary><b>3. Viewing All Entries</b></summary>



Displays all saved journal entries in a clean, chronological format.



<img src="unnamed(2).png" alt="View Entries">
</details>

<details>
<summary><b>4. Advanced Keyword Search</b></summary>



Efficiently filter through your history to find specific mentions or dates.



<img src="ab01dc06-9111-4425-ad64-ae729f994688.png" alt="Search Entry">
</details>

<details>
<summary><b>5. Secure Data Deletion</b></summary>



Includes a confirmation prompt to prevent accidental data loss.



<img src="d06ec630-e1ee-46e4-8613-9e98d04994ed.png" alt="Delete Entries">
</details>

<details>
<summary><b>6. Error Handling & Exit</b></summary>



Graceful handling of invalid inputs and professional termination messages.



<img src="5d3f8da4-b6cc-4bff-9779-f990ecd06d57.png" alt="Invalid Option">



<img src="7e60d67d-e0bc-4843-a444-8349a7ab60c8.png" alt="Exit Program">
</details>

📂 Project Architecture
The project follows a modular Object-Oriented approach for better maintainability.

Plaintext
📦 Personal-Journal-Manager
 ┣ 📜 File Operator.py  # Main Logic & Class Definition
 ┣ 📜 journal.txt       # Local Data Storage (Auto-generated)
 ┗ 📜 README.md         # Documentation
⚙️ How to Run
Prerequisites
Ensure Python 3.10 or higher is installed.

Ensure Python is added to your Windows PATH.

Steps to Execute
Open Command Prompt (cmd) or PowerShell.

Navigate to the directory containing the file.

Run the application using either command:

Bash
python "File Operator.py"
or

Bash
py "File Operator.py"
🧠 Concepts Demonstrated
Object-Oriented Programming (OOP): Encapsulation of logic within the JournalManager class.

File I/O Handling: Reading from and appending to local text files.

Exception Handling: Using try-except blocks to manage FileNotFoundError.

Control Flow: Implementation of match-case statements (Python 3.10+ feature).

📈 Future Improvements
[ ] Timestamping: Automatically add dates and times to every entry.

[ ] Encryption: Implement basic XOR or Fernet encryption for privacy.

[ ] Export Options: Ability to export the journal as a PDF or CSV file.

⚖️ License
This project is licensed under the MIT License – feel free to use and modify it for your own needs.

Developed with ❤️ for organized living.