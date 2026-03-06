# Dockerized Task Management Application

A task management web application built with **Flask** that allows users to create, prioritize, complete, and manage tasks.  
The application is containerized using **Docker** to ensure consistent runtime environments and includes a **CI/CD pipeline using GitHub Actions** for automated builds.

---

## Features

- Create and manage tasks
- Task prioritization (Low, Medium, High)
- Mark tasks as completed
- Undo completed tasks
- Delete tasks
- Task filtering (All, Active, Completed, High Priority)
- Task completion statistics

---

## Tech Stack

- **Backend:** Python, Flask
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Version Control:** Git, GitHub

---

## Docker Setup

Build the Docker image:

```
docker build -t taskflow-app .
```

Run the container:

```
docker run -p 5000:5000 taskflow-app
```

Access the application:

```
http://localhost:5000
```

---

## CI/CD Pipeline

This project uses **GitHub Actions** for continuous integration.

Workflow:

```
Push Code → GitHub Actions → Install Dependencies → Build Docker Image
```

The pipeline automatically runs whenever code is pushed to the `main` branch.

---

## Project Structure

```
docker-task-manager
│
├── app.py
├── Dockerfile
├── requirements.txt
├── templates
│
└── .github
     └── workflows
          └── ci.yml
```

---

## Author

Ankit Kumar  
GitHub: https://github.com/Ankit-codes87