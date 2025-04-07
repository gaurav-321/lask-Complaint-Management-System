# Lask Complaint Management System 📝

## Description
Lask is a web application designed to streamline complaint management within an organization. It offers features like user authentication, complaint submission, status updates, and administrative controls for managing users and departments. This system aims to enhance communication and efficiency in handling complaints.

## Features
- **User Authentication**: Secure login and registration.
- **Complaint Submission**: Submit complaints with optional media files.
- **Complaint Management**: View, filter, and update complaint statuses.
- **Admin Dashboard**: Manage users and departments.

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gag3301v/lask-Complaint-Management-System.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd lask-Complaint-Management-System
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Initialize the database**:
   ```bash
   python app.py db init
   python app.py db migrate
   python app.py db upgrade
   ```

6. **Run the application**:
   ```bash
   flask run
   ```

## Usage
Here’s how you can use the Lask Complaint Management System:

### User Registration
```python
from forms import RegistrationForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Handle user registration logic here
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
```

### Submitting a Complaint
```python
from forms import ComplaintForm

@app.route('/submit_complaint', methods=['GET', 'POST'])
@login_required
def submit_complaint():
    form = ComplaintForm()
    if form.validate_on_submit():
        # Handle complaint submission logic here
        return redirect(url_for('home'))
    return render_template('submit_complaint.html', title='Submit Complaint', form=form)
```

### Admin Dashboard
```python
@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'Admin':
        abort(403)
    # Handle admin dashboard logic here
    return render_template('admin.html', title='Admin Dashboard')
```

## Configuration
- **Environment Variables**:
  - `SECRET_KEY`: A secret key used for securely signing the session cookie.
  - `SQLALCHEMY_DATABASE_URI`: The database URI for SQLAlchemy.

## Tests
To run tests, use the following command:
```bash
python -m unittest discover tests
```

## Contributing
Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) to get started.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to explore and customize the Lask Complaint Management System according to your needs! 🚀