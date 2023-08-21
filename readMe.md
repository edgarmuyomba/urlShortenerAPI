# URL Shortener API using Django Rest Framework

This project is a URL shortener API built using Django Rest Framework. The API allows users to submit long URLs and receive shorter versions that are mapped to the original URLs through a database. It includes validation to ensure that only valid URLs are submitted, and it prevents duplicate URLs from being stored. Additionally, the project utilizes `django-cors-headers` to manage and verify access to the API from different origin URLs.

## Features

- Shorten long URLs into easily shareable short URLs.
- Prevent duplicate URLs from being stored in the database.
- Validate submitted URLs to ensure they are in the correct format.
- Manage and control cross-origin resource sharing (CORS) using `django-cors-headers`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/edgarmuyomba/urlShortenerAPI.git
   cd urlShortenerAPI
   ```
2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```
4. Setup the database
    ```bash
    python manage.py runserver
    ```
5. Access the API at `http://127.0.0.1:8000/` in your browser or API client.

## API Endpoints
- `POST /api/shorten/`
    - Description: Submit a URL to be shortened.
    - Request Body:
    ```bash
    {
        "source": "https://www.example.com/long-url"
    }
    ```
    - Reponse
    ```bash
    {
        "tiny": "http://127.0.0.1:8000/<int>/"
    }
    ```
- `GET /s/{short_code}`
    - Description: Redirect to the original URL associated with the provided short code.

## CORS Configuration
The project uses `django-cors-headers` to manage cross-origin resource sharing. By default, the CORS configuration allows requests from all origins. You can modify the `CORS_ALLOW_ALL_ORIGINS` setting in settings.py to restrict access to specific origins
```bash
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8001",
    "https://your-frontend-domain.com",
]
```
