
---

```
Little Lemon Restaurant Web Application
========================================

Overview
--------
This web application is the backend for the **Little Lemon Restaurant**, built using Django and Django REST Framework (DRF). It allows users to interact with the restaurant's table booking system via a REST API.

Key Features:
- User Registration and Authentication: Register, log in, and manage sessions securely.
- Menu Management: Perform CRUD operations to manage menu items.
- Table Booking API: Book tables and view available slots.
- User Authorization: JWT-based authentication ensures secure access.

Setup Instructions
------------------
### Requirements:
1. Python 3.x
2. Django 3.x
3. MySQL database (or SQLite as a fallback)

### Installation:

1. Clone the repository:
   ```
   git clone https://github.com/oladokedamilola/littlelemon.git
   ```

2. Navigate to the project directory:
   ```
   cd littlelemon
   ```

3. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

API Endpoints
-------------
### User Authentication:
- **Register a User** (`POST /auth/users/`):
  ```
  {
    "username": "testuser",
    "password": "password123",
    "email": "test@example.com"
  }
  ```

- **Login** (`POST /auth/token/login/`):
  ```
  {
    "username": "testuser",
    "password": "password123"
  }
  ```
  Response:
  ```
  {
    "auth_token": "your_generated_token_here"
  }
  ```

- **Logout** (`POST /auth/token/logout/`):
  No payload required.

### Table Booking API:
- **Create a Booking** (`POST /api/bookings/`):
  ```
  {
    "user": 1,
    "table_number": 5,
    "date_time": "2024-12-01T18:00:00Z"
  }
  ```

- **View All Bookings** (`GET /api/bookings/`):
  Response:
  ```
  [
    {
      "user": 1,
      "table_number": 5,
      "date_time": "2024-12-01T18:00:00Z"
    }
  ]
  ```

- **Update a Booking** (`PUT /api/bookings/{id}/`):
  ```
  {
    "table_number": 6,
    "date_time": "2024-12-01T20:00:00Z"
  }
  ```

- **Delete a Booking** (`DELETE /api/bookings/{id}/`):
  No payload required.

### Menu Management API:
- **View Menu Items** (`GET /api/menu/`):
  Response:
  ```
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
  ```
  {
    "title": "Pasta",
    "price": 8.99,
    "inventory": 30
  }
  ```

- **Update a Menu Item** (`PUT /api/menu/{id}/`):
  ```
  {
    "title": "Salad",
    "price": 7.99,
    "inventory": 25
  }
  ```

- **Delete a Menu Item** (`DELETE /api/menu/{id}/`):
  No payload required.

---

**Note**: Replace all placeholder values (e.g., user IDs, tokens) with actual data from your implementation.

---
