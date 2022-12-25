# Flask Complaint Management System
A Flask-based web application for managing and tracking complaints, with optional media file attachments.

## Features
- Login and registration for users
- Submission of complaints with optional media files
- Viewing and filtering of complaints by status (resolved/unresolved)
- Updating the status of complaints
- Viewing and modifying user and department information (for admins)
## Requirements
- Python 3
- Flask
- SQLAlchemy
## Running the app
1. Clone the repository
2. Install the required packages using pip install -r requirements.txt
3. Run the app using python app.py
4. Navigate to http://localhost:5000 in your browser to access the app
## Routes
- /: Home page
- /login: Login page
- /register: Register page
- /send_complaint: Submission page for complaints
- /complaint: View all complaints
- /complaint/<id>: View a specific complaint
- /update_status: Update the status of a complaint
- /logout: Logout page
- /unauthorized: Page displayed when attempting to access a protected route without proper authorization
- /admin: Admin dashboard (view and modify users and departments)
