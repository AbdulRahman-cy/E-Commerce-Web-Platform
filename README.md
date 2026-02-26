# 🛒 E-Commerce Auction & Trading Platform

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0.2-green.svg)](https://www.djangoproject.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)

A robust, backend-focused e-commerce application designed for real-time auctioning and category-based trading. This project demonstrates a transition from traditional multi-page applications to a modern, containerized architecture using AJAX for seamless user experiences.

## 📑 Table of Contents 🧠 These aren't just feature descriptions. Each section reflects a genuine technical challenge I faced, researched, and solved myself.

* [🏛️ System Architecture](#-system-architecture)
* [🎨 Frontend Engineering & UI Logic](#-frontend-engineering--ui-logic)
* [⚙️ Backend Engineering & Data Integrity](#-backend-engineering--data-integrity)
* [🚀 DevOps & Deployment (Docker)](#-devops--deployment-docker)
* [📸 Project Gallery](#-project-gallery--proof-of-work)

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

---

## 🎨 Frontend Engineering & UI Logic

The frontend was built with a "Performance-First" mindset, moving away from hardcoded logic toward a dynamic interface.

> [!IMPORTANT]
> **Global Data Persistence: Context Processors**
> 
> One of my biggest challenges was the **Floating Cart**. I wanted the cart and its item count to be visible on every single page, but I didn't want to manually query the database in every single view function.
> 
> * **The Problem:** Passing cart data to every `render()` function was repetitive and prone to errors.
> * **The Solution:** I researched and found **Context Processors**. This allows the cart object to be globally available to all templates automatically.
> * **Key Learning:** This kept my views clean and ensured I wasn't using redundant code across my templates.

> [!IMPORTANT]
> **Jinja Templates & Database Constraints**
> 
> I learned the hard way that Jinja templates do not support direct database access for security and performance reasons.
> 
> * **The Solution:** I used **Custom Template Tags** and a **dictionary-based lookup (`cart_map`)**. Instead of running a query for every item in the frontend (which is impossible), I pass a pre-mapped dictionary from the backend.
> * **The Result:** Zero errors and drastically improved page load speeds by keeping logic in the Python layer.

```html
<span id="qty-{{ item.id }}">
    {{ cart_map|get_item:item.id|default:1 }}
</span>
```

> [!IMPORTANT]
> **JavaScript Isolation & The DRY Principle**
> 
> Initially, I was writing similar scripts for "Likes" and "Add to Cart" on different pages. I realized I was violating the **DRY (Don't Repeat Yourself)** principle.
> 
> * **The Problem:** Redundant code in multiple `<script>` tags was a maintenance nightmare.
> * **The Solution:** I **isolated the JavaScript** into a single, modular file. I moved from specific element selectors to **Event Delegation**.
> * **Technical Takeaway:** I learned that `querySelectorAll` returns a **static NodeList**. By using event delegation on a parent container, I can handle clicks even on elements added dynamically via AJAX without adding 50+ expensive event listeners.

> [!IMPORTANT]
> **UI Refinement: Absolute Positioning & UX**
> 
> The "Floating Cart" and "Category Selection" badges initially overlapped. I mastered CSS **Absolute and Fixed positioning**, `z-index`, and offsets to ensure a clean visual hierarchy regardless of screen size.

---

## ⚙️ Backend Engineering & Data Integrity

I prioritized making the database the "Source of Truth" to prevent invalid data states.

> [!IMPORTANT]
> **Database-Level Constraints & Unique Logic**
> 
> I needed to ensure a user could not "Watch" the same listing multiple times.
> 
> * **The Problem:** Preventing duplicate entries through Python logic alone can lead to **Race Conditions**.
> * **The Solution:** I implemented **Unique Constraints** directly in the Django Models using `unique_together`.

```python
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    
    class Meta:
        # Enforces that one user can only watch a specific listing once
        unique_together = ('user', 'listing')
```

> [!IMPORTANT]
> **Advanced Many-to-Many Architecture**
> 
> Instead of a simple `ManyToManyField`, I built a **Custom Intermediate Model** for relationships like "Watchlists" and "Likes".
> 
> * **The Reasoning:** A standard M2M is hidden. An intermediate model allows me to store vital metadata.
> * **The Benefit:** I can now track **when** (`created_at`) a user added an item, enabling "Recently Added" sorting.

```python
class Watchlist(models.Model):
    user = models.ForeignKey(User, related_name="watchlist", on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # Metadata not possible in standard M2M
```

> [!IMPORTANT]
> **Dynamic Mapping with Context Processors**
> 
> I built a custom Context Processor that automatically injects the user's current cart and bid counts into every request context. This removed redundant database queries from **12 different view functions**, drastically simplifying the `views.py` file.

---

## 📸 Project Gallery & Proof of Work

![Screenshot 1](screenshots/Screenshot%202026-02-26%20060707.png)
![Screenshot 2](screenshots/Screenshot%202026-02-26%20060748.png)
![Screenshot 3](screenshots/Screenshot%202026-02-26%20060856.png)
![Screenshot 4](screenshots/Screenshot%202026-02-26%20060913.png)
![Screenshot 5](screenshots/Screenshot%202026-02-26%20060946.png)
![Screenshot 6](screenshots/Screenshot%202026-02-26%20061018.png)
![Screenshot 7](screenshots/Screenshot%202026-02-26%20061035.png)
