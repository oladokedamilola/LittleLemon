---

# Little Lemon Restaurant Web Application

## Overview

This web application is the backend for the **Little Lemon Restaurant** using Django and Django REST Framework (DRF). It enables users to interact with the restaurant's table booking system via a REST API.

### Key Features:
- **User Registration and Authentication**: Allows users to register, login, and manage sessions.
- **Menu Management**: CRUD operations to manage menu items.
- **Table Booking API**: Allows customers to book tables and view available slots.
- **User Authorization**: JWT-based authentication for secure access to the API.

## Setup Instructions

### Requirements:
1. Python 3.x
2. Django 3.x
3. MySQL database (or SQLite as a fallback)

### Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/oladokedamilola/littlelemon.git
   ```

2. Navigate to the project directory:

   ```bash
   cd littlelemon
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints to Test

### User Authentication

- **Register a User** (`POST /auth/users/`):
  - Example payload:
    ```json
    {
      "username": "testuser",
      "password": "password123",
      "email": "test@example.com"
    }
    ```
  
- **Login (Get Auth Token)** (`POST /auth/token/login/`):
  - Example payload:
    ```json
    {
      "username": "testuser",
      "password": "password123"
    }
    ```
  - Response:
    ```json
    {
      "auth_token": "your_generated_token_here"
    }
    ```

- **Logout (Revoke Token)** (`POST /auth/token/logout/`):
  - No payload required.

### Table Booking API

- **Create a Booking** (`POST /api/bookings/`):
  - Example payload:
    ```json
    {
      "user": 1,  # User ID from the registration
      "table_number": 5,
      "date_time": "2024-12-01T18:00:00Z"
    }
    ```

- **View All Bookings** (`GET /api/bookings/`):
  - Response:
    ```json
    [
      {
        "user": 1,
        "table_number": 5,
        "date_time": "2024-12-01T18:00:00Z"
      }
    ]
    ```

- **Update a Booking** (`PUT /api/bookings/{id}/`):
  - Example payload:
    ```json
    {
      "table_number": 6,
      "date_time": "2024-12-01T20:00:00Z"
    }
    ```

- **Delete a Booking** (`DELETE /api/bookings/{id}/`):
  - No payload required.

### Menu Management API

- **View Menu Items** (`GET /api/menu/`):
  - Response:
    ```json
    [
      {
        "id": 1,
        "title": "Pizza",
        "price": 10.99,
        "inventory": 50
      }
    ]
    ```

- **Create a Menu Item** (`POST /api/menu/`):
  - Example payload:
    ```json
    {
      "title": "Pasta",
      "price": 8.99,
      "inventory": 30
    }
    ```

- **Update a Menu Item** (`PUT /api/menu/{id}/`):
  - Example payload:
    ```json
    {
      "title": "Salad",
      "price": 7.99,
      "inventory": 25
    }
    ```

- **Delete a Menu Item** (`DELETE /api/menu/{id}/`):
  - No payload required.

---

