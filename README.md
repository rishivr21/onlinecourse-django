# Online Course Django Application

## Overview

This project is a **Django-based Online Course Application** that allows users to explore courses, view lessons, take mock exams, and receive automated results after submission. The system demonstrates how Django models, views, templates, and URL routing work together to create a functional web application.

The application also includes an administrative interface where instructors can manage courses, lessons, questions, and exam choices.

## Features

* Course and lesson management
* Mock exam functionality
* Automatic exam evaluation
* Result page displaying score and correct answers
* Django admin dashboard for managing application data
* Bootstrap-based responsive interface

## Technologies Used

* Python
* Django
* HTML
* Bootstrap
* SQLite Database

## Application Structure

The application follows the standard Django architecture:

* **Models** – Define the database structure for courses, lessons, questions, choices, and submissions.
* **Views** – Handle the logic for exam submission and result evaluation.
* **Templates** – Render the course details and exam results using Django template tags.
* **URLs** – Route requests to the appropriate views.
* **Admin Panel** – Manage all application data through Django's built-in admin interface.

## Running the Project

### 1. Install Django

```
pip install django
```

### 2. Apply Migrations

```
python manage.py migrate
```

### 3. Create Admin User

```
python manage.py createsuperuser
```

### 4. Run the Development Server

```
python manage.py runserver
```

### 5. Open the Application

```
http://127.0.0.1:8000/
```

## Author

**Rishikant Verma**

GitHub: https://github.com/rishivr21
