# Employee Management API

**Live Demo:** [https://employee-api-yrj7.onrender.com](https://employee-api-yrj7.onrender.com)

A robust REST API built with Django Rest Framework for managing employee records. This project features JWT authentication, beautiful interactive documentation (Swagger UI), and is ready for deployment on Render.

## Features

- **Authentication**: Supports both internal Session Authentication (for Browsable API) and JWT Authentication (for external clients).
- **Interactive Documentation**: Integrated Swagger UI (`drf-spectacular`) for exploring and testing the API.
- **CRUD Operations**: Full Create, Read, Update, Delete support for Employee records.
- **Filtering & Pagination**: Built-in support for filtering by department/role and pagination.
- **Production Ready**: Configured for Render deployment with `Whitenoise` and `PostgreSQL` support.
- **Comprehensive Testing**: Automated test suite for all API endpoints using `pytest`.

## Quick Start

### 1. Install Dependencies
This project works with standard `pip` or `uv`.

```bash
uv sync  # or pip install -r requirements.txt
```

### 2. Apply Migrations
```bash
python src/manage.py migrate
```

### 3. Create Demo User
To access the protected routes, you will need a user account.
```bash
python src/manage.py createsuperuser
# Follow prompts. For demo purposes, you can use:
# Username: admin
# Password: admin123
```

### 4. Run Server
```bash
python src/manage.py runserver
```

## Running Tests
This project includes comprehensive automated tests for all API endpoints using `pytest`.

```bash
uv run pytest
```

## API Documentation (Swagger UI)

Navigate to the **Base URL** (e.g., `http://127.0.0.1:8000/`) to see the interactive API documentation.

### How to use Swagger UI:
1.  **Authorize**: Click the **Authorize** button.
    *   **Option A (`cookieAuth`)**: If you are logged in via the Django Admin or "Log in" button, this works automatically.
    *   **Option B (`Bearer`)**: Send a POST request to `/api/token/` to get an `access` token. Enter `Bearer <your_token>` in the authorize box.
2.  **Test Endpoints**: Click on any endpoint (e.g., `GET /api/employees/`), click **Try it out**, then **Execute**.

## Authentication & Credentials

To test the API quickly, you can use the built-in login view or generating a token.

**Demo Credentials (Live & Local):**
Use these credentials to log in to the **Live Demo** or your local instance (if created):

*   **Username**: `admin`
*   **Password**: `admin123`

*(Note: On the live demo, this user is automatically created on deployment. Locally, run `createsuperuser`)*

## API Routes

| HTTP Method | Endpoint | Description | Access |
| :--- | :--- | :--- | :--- |
| **GET** | `/` | **Swagger UI Documentation** | Public |
| **POST** | `/api/token/` | Get JWT Access & Refresh Tokens | Public |
| **POST** | `/api/token/refresh/` | Refresh Access Token | Public |
| **GET** | `/api/employees/` | List all employees (paginated) | Authenticated |
| **POST** | `/api/employees/` | Create a new employee | Authenticated |
| **GET** | `/api/employees/{id}/` | Get details of specific employee | Authenticated |
| **PUT** | `/api/employees/{id}/` | Update an entire employee record | Authenticated |
| **PATCH** | `/api/employees/{id}/` | Partially update an employee record | Authenticated |
| **DELETE** | `/api/employees/{id}/` | Delete an employee | Authenticated |
| **GET** | `/api/schema/` | OpenAPI 3.0 Schema (YAML) | Public |

## Deployment (Render)

This project is configured for [Render.com](https://render.com).

1.  **Build Command**: `./build.sh`
2.  **Start Command**: `gunicorn --chdir src core.wsgi:application`
3.  **Environment Variables**:
    *   `SECRET_KEY`: (Random String)
    *   `PYTHON_VERSION`: `3.11.0`
    *   `DATABASE_URL`: (Auto-set if linking a Render Postgres DB)
