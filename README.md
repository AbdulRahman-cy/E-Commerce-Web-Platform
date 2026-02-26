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

## 🎨 Frontend Engineering & UI Logic

The frontend of this auction platform was built with a "Performance-First" mindset. My main goal was to move away from hardcoded, redundant logic toward a dynamic, data-driven interface.

### **[Important] Global Data Persistence: Context Processors**
One of my biggest challenges was the **Floating Cart**. I wanted the cart and its item count to be visible on every single page (Index, Categories, Watchlist), but I didn't want to manually query the database in every single view function.

* **The Problem:** Passing cart data to every `render()` function was repetitive and prone to errors.
* **The Solution:** I implemented a **Context Processor**. This allows the cart object to be globally available to all templates automatically. 
* **Key Learning:** This kept my views clean and ensured the UI always stayed in sync with the user's session.

### **[Important] Intelligent Templating: Custom Template Tags**
Handling queries for dozens of listings on a single page (like checking if an item is already in a user's cart) threatened to make my templates messy and slow.

* **The Solution:** I created a custom template tag and used a **dictionary-based lookup (`cart_map`)**. Instead of running a query for every item, I pass a pre-mapped dictionary to the frontend.
* **Code Example:**
    ```html
    <span id="qty-{{ item.id }}">
        {{ cart_map|get_item:item.id|default:1 }}
    </span>
    ```
* **The Result:** Drastically reduced template logic complexity and improved page load speeds.

### **[Important] JavaScript Isolation & The DRY Principle**
Initially, I found myself writing similar JavaScript for "Likes" on the index page and "Watchlist" buttons on the listing pages. I realized I was violating the **DRY (Don't Repeat Yourself)** principle.

* **The Problem:** Redundant code in multiple `<script>` tags was a maintenance nightmare.
* **The Solution:** I **isolated the JavaScript**. I consolidated the shared logic into a single, modular JS file. I moved from specific element selectors to **Event Delegation**, allowing one script to handle interactions across the entire site.
* **Technical Takeaway:** I learned that `querySelectorAll` returns a **static NodeList**, and by using event delegation, I could handle clicks even on elements that were added to the DOM dynamically via AJAX.

### **[Important] UI Refinement: Absolute Positioning & UX**
The "Floating Cart" button and the "Category Selection" badges initially overlapped, creating a cluttered and "broken" feel.
* **The Fix:** I mastered CSS **Absolute and Fixed positioning** to ensure a clean visual hierarchy. I used `z-index` and calculated offsets to make sure these elements exist in their own space without colliding, regardless of screen size.
