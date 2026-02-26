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

* 🧠 Key Takeaways & Engineering Growth
🎨 Frontend Development
Domain Focus: JavaScript Architecture & UI Polish

[CRITICAL] Architectural Shift: Event Delegation vs. forEach Loops

I learned to move away from attaching individual event listeners to elements using forEach. While simpler for small tasks, it creates massive side effects when the DOM is dynamic (e.g., when AJAX removes or adds items).

Solution: I implemented Event Delegation, attaching a single listener to a parent container. This ensures that even if a "Remove All" button or a cart item is deleted/re-added, the logic remains functional without needing to re-bind listeners.

[IMPORTANT] DOM Manipulation & NodeLists

I discovered that querySelectorAll returns a static NodeList, not a live array. Understanding this distinction was vital for correctly updating cart counts and UI badges without "ghost" data remaining in the view.

[IMPORTANT] AJAX & The "Vanishing" Logic

Learned how to coordinate backend state changes with frontend physical DOM removal. I implemented logic to physically remove items from the document tree once the quantity reached zero, ensuring a "Single Source of Truth" between the server and the user's screen.

[MODERATE] CSS & UI Hierarchy

Mastered the use of z-index and absolute/fixed positioning to prevent overlap between floating UI elements (like the Cart button and Category badges).

⚙️ Backend Development
Domain Focus: Django Logic & Data Integrity

[CRITICAL] Custom Template Tags & Filtering

Developed custom logic to handle cart mapping within templates, allowing the backend to pass complex data structures that the frontend can easily consume and display.

[IMPORTANT] Model Logic for E-Commerce

Refined the relationship between Listings, Carts, and Bids. I learned how to handle edge cases in bidding logic to ensure data integrity during real-time auctions.

[MODERATE] Django-to-JS Communication

Learned to use data-* attributes in HTML to safely pass Django variables (like URLs and IDs) to external JavaScript files, keeping the logic separated from the markup.

🐳 DevOps & Environment
Domain Focus: Containerization & Security

[CRITICAL] Environment Isolation & The "Venv" vs. "Docker" Conflict

I learned that while a local Virtual Environment (VE) is great for IDE support, Docker is the ultimate truth. I mastered the separation between my Windows host machine and the Linux container environment.

[CRITICAL] Security & Image Optimization via .dockerignore

Understood the vital role of the .dockerignore file. Beyond just saving space, it is a security necessity—preventing the .git folder (containing sensitive history) and local db.sqlite3 files from being "baked" into public images.

[IMPORTANT] Dependency Management with pipreqs

Discovered how to use pipreqs to scan project imports and generate a minimalist requirements.txt. This avoids "image bloat" by ensuring only the necessary libraries (like Django and Pillow) are installed.

[MODERATE] Persistence via Docker Volumes

Configured volume mapping in docker-compose to ensure that even when the container is "destroyed," the SQLite database survives on my local machine.
