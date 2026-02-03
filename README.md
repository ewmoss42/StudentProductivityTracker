Student Productivity Tracker Web App

Instructions for Build and Use

Software Demo

📹 Demo Video:
(Paste your YouTube video link here)

Steps to Build and/or Run the Software

Create a project folder and open it in Visual Studio Code.

Create and activate a virtual environment:

Mac:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

Install Flask:

pip install flask

Run the web application:

python3 app.py

Open a browser and go to:

http://127.0.0.1:5000

Instructions for Using the Software

Use the task form to add a new assignment or task.

Click “Mark Complete” to mark a task as finished.

Click “Undo” to return a task to active status.

Use the filters to view all tasks, active tasks, or completed tasks.

Click “Delete” to remove a task.

Development Environment

To recreate the development environment, you will need:

Python 3.9+

Flask

SQLite (built into Python)

Visual Studio Code (or another code editor)

Useful Websites to Learn More

The following resources were helpful during development:

Flask Documentation
https://flask.palletsprojects.com/

Python sqlite3 Documentation
https://docs.python.org/3/library/sqlite3.html

Future Work

Planned improvements and extensions for this project include:

Adding user authentication and accounts

Task categories and priority levels

Calendar or deadline reminders

Cloud database support

Mobile-friendly responsive interface