# 📊 Financial Portfolio Management System

A web-based **Financial Portfolio Management System** built using **Python (Django)** that helps users manage and track their investment portfolios including stocks, REITs, ETFs, and other financial assets.

---

## 🚀 Features
- User authentication and authorization
- Manage investment portfolios
- Track assets and transactions
- Integration with financial data services
- Asynchronous task handling using Celery
- PostgreSQL database support
- Docker-based deployment support

---

## 🛠️ Tech Stack
- **Backend:** Python 3.8, Django 3.1.3
- **Database:** PostgreSQL
- **Task Queue:** Celery
- **Message Broker:** RabbitMQ
- **Cache / Result Backend:** Redis
- **Deployment:** Docker, Heroku
- **Environment Management:** Pipenv

---

## 📂 Project Structure

financial-portfolio-management-system/

├── finance/                         # Main Django project configuration
   ├── __init__.py
   ├── settings.py                  # Project settings
   ├── urls.py                      # Root URL configurations
   ├── asgi.py                      # ASGI entry point
   ├── wsgi.py                      # WSGI entry point
   └── celery.py                    # Celery configuration
├── portfolio/                       # Portfolio management app
   ├── migrations/                  # Database migrations
   ├── management/
   ├── templates/                   # HTML templates
   ├── admin/                       # Admin-related customizations
   ├── templatetags/                # Custom template tags
   ├── tests/                       # Test cases
   ├── __init__.py
   ├── admin.py                     # Django admin configuration
   ├── apps.py                      # App configuration
   ├── constants.py                 # Application constants
   ├── forms.py                     # Django forms
   ├── models.py                    # Database models
   ├── selectors.py                 # Query logic / selectors
   ├── services.py                  # Business logic services
   ├── signals.py                   # Django signals
   ├── tasks.py                     # Celery background tasks
   ├── views.py                     # Application views
   └── urls.py                      # App-level URL routing
├── static/                          # Static files (CSS, JS, Images)
├── .env                             # Environment variables
├── .gitignore                       # Git ignored files
├── app.json                         # Heroku app configuration
├── docker-compose-dev.yml           # Docker Compose (development)
├── Dockerfile                       # Docker image definition
├── heroku.yml                       # Heroku deployment configuration
├── manage.py                        # Django management script
├── Pipfile                          # Python dependencies
├── Pipfile.lock                     # Locked dependencies
└── README.md                        # Project documentation


---

## ✅ Prerequisites
Make sure you have the following installed:
- Python 3.8
- PostgreSQL
- Pipenv
- Docker (optional but recommended)

---

## ⚙️ Installation (Without Docker)

### 1️⃣ Install dependencies
pipenv install

### 2️⃣ Activate virtual environment
pipenv shell

### 3️⃣ Configure environment variables
Update the .env file according to your local setup (database credentials, secret key, etc).

### 4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

### 5️⃣ Create superuser
python manage.py createsuperuser

### 6️⃣ Start the development server
python manage.py runserver

🌐 Open browser:
http://127.0.0.1:8000

## ⚙️ Installation (Using Docker)

### 1️⃣ Run Docker Compose
docker-compose -f docker-compose-dev.yml up

### 2️⃣ Access the application
http://localhost:8000

Docker automatically sets up:
Django
PostgreSQL
Celery
Redis
RabbitMQ

## 🧪 Future Enhancements
- AI-based investment insights
- Portfolio performance analytics
- Risk assessment module
- Interactive charts and dashboards
- REST API integration

## 👨‍💻 Author
**Dev Patel**
