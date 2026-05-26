# Contact Book

A web application built with Python, Flask, and SQLite.

## Live Demo
https://web-production-42e0f.up.railway.app/contacts

## Features
- View all contacts
- Add a new contact
- Search contacts by name
- Amend an existing contact
- Delete a contact

## Tech Stack
- Python
- Flask
- SQLite
- Jinja2 HTML templates
- pytest

## How to Run
1. Clone the repo
2. Activate virtual environment: myenv\Scripts\activate
3. Install dependencies: pip install -r requirements.txt
4. Run the app: python app.py
5. Open browser: http://127.0.0.1:5000/contacts

## Deployment
Deployed on Railway using Gunicorn as the production server.

## Tests
Run with: pytest test_contacts.py
