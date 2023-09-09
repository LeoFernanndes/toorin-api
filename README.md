# toorin_api
Bookstore management api implemented with django rest framework

## Python version
3.9.14

## Instructions
1. Clone the repository
2. Create a virtual environment inside the cloned repository
    python3 -m venv venv (creates virtual environment)
    source venv/bin/activate (activates virtual environment)
3. Install dependencies
    pip install -r requirements.txt
4. Execute migrations
    python manage.py migrate
5. Load initial data
    python manage.py loaddata users tipoacesso
6. Execute the tests
    python manage.py test
6. Start development server
    python manage.py runserver 0.0.0.0:8000

## Environment variables
Create a .env file inside clone repository
    DB_NAME=toorin\
    DB_USER=admin\
    DB_PASSWORD=password\
    DB_HOST=127.0.0.1\
    DB_PORT=5432

## Admin user
username: username
password: password123