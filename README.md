# Django Task Manager

A simple task management application built with Django, designed to demonstrate full-stack web development fundamentals.  
This project includes user authentication, CRUD operations, basic styling, and automated testing.

## Features

- User registration, login, and logout functionality
- Create, read, update, and delete personal tasks
- Secure view access for authenticated users only
- Basic HTML templating with reusable `base.html`
- Light CSS styling for improved user experience
- Unit tests for authentication flow and task management

## Technologies Used

- Python 3.7+
- Django 4.x
- SQLite (default development database)
- HTML5 and CSS3
- Git and GitHub for version control

## Installation Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR-USERNAME/django-task-manager.git
    ```

2. **Navigate into the project directory:**

    ```bash
    cd django-task-manager
    ```

3. **Set up a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    source .venv/bin/activate    # On Mac/Linux
    .venv\Scripts\activate       # On Windows
    ```

4. **Install required dependencies:**

    ```bash
    pip install django
    ```

    (Optional: If using a `requirements.txt`, install with `pip install -r requirements.txt`.)

5. **Apply migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the app in your browser:**

    ```
    http://127.0.0.1:8000/tasks/
    ```

## Running Tests

Basic unit tests are included to verify critical functionality:

```bash
python manage.py test
