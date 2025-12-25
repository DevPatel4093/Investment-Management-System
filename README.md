# 📊 Investment Management System

A web-based **Investment Management System** built using **Python (Django)** that helps users manage and track their investment portfolios including stocks, REITs, ETFs, and other financial assets.

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
```
investment-management-system/
├── finance/   
├── portfolio/                
├── static/                          
├── .env                             
├── .gitignore                       
├── app.json                         
├── docker-compose-dev.yml           
├── Dockerfile                      
├── heroku.yml                       
├── manage.py                       
├── Pipfile                         
├── Pipfile.lock                     
└── README.md                        
```

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
