# Dogtor (Django Edition)

A Django-based web application to manage pet owners, veterinarians, informational blog posts, user authentication, and more. This project was built for educational purposes to demonstrate entity relationships using the Django REST Framework.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Requirements](#requirements)
- [Contribution](#contribution)
- [Learn More](#learn-more)

---

## Project Structure

```
dogtor/
├── api/                  # Business logic and main endpoints
├── authentification/     # User registration and authentication
├── blog/                 # Informational blog module
├── vet/                  # Veterinarian management
├── dogtor/               # Main Django project configuration
├── templates/            # HTML templates
├── manage.py             # Main script for Django commands
├── requirements.txt      # Project dependencies
```

---

## Features

- User registration and login with custom roles
- RESTful API for managing pets, appointments, users, and vets
- Informational blog module
- Extended admin panel
- PostgreSQL integration
- Token-based authentication (can be extended with JWT)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/LSCasas/dogtor_django.git
   cd dogtor
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Apply migrations and create a superuser:**

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

---

## How to Use

### Example Endpoints (with `curl` or Postman)

**1. List all veterinarians:**

```bash
curl http://localhost:8000/vet/
```

**2. Create a new veterinarian (POST):**

```bash
curl -X POST -d "nombre=Dr. John&especialidad=Dentistry&telefono=555-9999" http://localhost:8000/vet/
```

**3. Authentication (if using token login system):**

```bash
curl -X POST -d "username=user&password=yourpassword" http://localhost:8000/auth/login/
```

---

## Requirements

- Python 3.x
- Django 5.1.4
- Django REST Framework 3.15.2
- PostgreSQL
- psycopg2-binary 2.9.10

---

## Contribution

1. Fork the repository.

2. Create a new branch:

   ```bash
   git checkout -b feature/my-feature
   ```

3. Make your changes and commit:

   ```bash
   git commit -am "Add new feature"
   ```

4. Push your branch:

   ```bash
   git push origin feature/my-feature
   ```

5. Open a Pull Request on GitHub.

---

## 📚 Learn More

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [psycopg2 for PostgreSQL](https://www.psycopg.org/)
- [Dotenv for Python](https://pypi.org/project/python-dotenv/)

---

Your feedback and contributions to this project are welcome!
