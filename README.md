# 🛒 E-Commerce Auction & Trading Platform

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.2-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)

A robust, backend-focused e-commerce application designed for real-time auctioning and category-based trading. This project demonstrates a transition from traditional multi-page applications to a modern, containerized architecture using AJAX for seamless user experiences.

---

## 🏛️ System Architecture

The application is built with a focus on **Separation of Concerns** and **Environment Parity**. It uses a containerized Linux environment to ensure that the code runs identically across any machine.



### Backend Core
* **Framework:** Django 5.0.2 (leveraging Class-Based Views and customized template tags)
* **Database:** SQLite with Docker volume persistence to prevent data loss during container restarts
* **Task Handling:** Custom logic for auction bid validation and expiration.

### Frontend Enhancements
* **AJAX Integration:** Implemented asynchronous requests for cart updates and "Remove All" logic, eliminating the need for full page reloads.
* **Responsive Styling:** Custom CSS with Bootstrap utilities, specifically optimized for UI/UX to prevent element overlap (e.g., Cart and Category floating badges).

---

## 🛠️ Tech Stack & Dependencies

| Category | Tools |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Framework** | Django |
| **Containerization** | Docker, Docker Compose |
| **Image Processing** | Pillow (used for dynamic Auction Listings) |
| **Frontend** | JavaScript (ES6+), Bootstrap 5, CSS3 |

---

## 🚀 DevOps & Deployment (Docker)

This project is fully dockerized to solve "it works on my machine" issues. 

### Key Docker Implementation Details:
* **Multi-stage-like Build logic:** The `Dockerfile` uses `python:3.12-slim` to minimize image size.
* **Security & Optimization:** A strict `.dockerignore` file excludes `venv/`, `.git/`, and `__pycache__` to prevent image bloat and secret leakage.
* **Volume Mapping:** Maps local source code to the `/app` directory inside the container for real-time development.
