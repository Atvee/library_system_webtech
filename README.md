# 📚 Library Management System

*A Django Web Application*

---

## 🌟 Overview

This project is a **full-stack web application** built using **Django** that simulates a simple library system.

It allows users to **manage books efficiently** with features like authentication and full CRUD operations.

> 💡 Built as a beginner-friendly project to understand how real-world web applications work.

---

## ✨ Features

* 🔐 User Authentication (Register / Login / Logout)
* 📖 View all books in the system
* ➕ Add new books
* ✏️ Edit existing books
* ❌ Delete books
* 👤 Track which user added each book
* 🛠️ Django Admin Panel for management

---

## 🧩 Tech Stack

* **Backend:** Django (Python)
* **Database:** SQLite (default)
* **Frontend:** HTML (Django Templates)
* **Authentication:** Django built-in auth system

---

## 🏗️ Project Structure

```
library_system/
│── library_system/   # Main project settings
│── books/            # App handling book logic
│   ├── models.py     # Database structure
│   ├── views.py      # Application logic
│   ├── forms.py      # Forms for input
│   ├── urls.py       # Routing
│   └── templates/    # HTML files
│── manage.py
```

---

## ⚙️ How It Works

### 🔹 1. Models (Database Layer)

The `Book` model defines how data is stored:

* Title
* Author
* Description
* Added by (User)

Django ORM automatically converts this into database tables.

---

### 🔹 2. Authentication System

* Users can register and log in
* Sessions keep users logged in
* Only authenticated users can access features

---

### 🔹 3. Views (Core Logic)

Views control the application behavior:

| View          | Purpose           |
| ------------- | ----------------- |
| `register`    | Create new user   |
| `book_list`   | Display all books |
| `book_create` | Add book          |
| `book_update` | Edit book         |
| `book_delete` | Delete book       |

---

### 🔹 4. CRUD Operations

| Action | Description         |
| ------ | ------------------- |
| Create | Add a new book      |
| Read   | View all books      |
| Update | Modify book details |
| Delete | Remove a book       |

---

### 🔹 5. Templates (UI)

The frontend is built using Django templates:

* Book listing page
* Form page (add/edit)
* Delete confirmation page
* Login & registration pages

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd library_system
```

### 2️⃣ Setup Environment

```bash
python -m venv library_env
source library_env/bin/activate   # Mac/Linux
library_env\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django
```

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

### 6️⃣ Start Server

```bash
python manage.py runserver
```

---

## 🌐 Usage

* Visit `/register/` → Create account
* Login to access dashboard
* Add, edit, or delete books
* Visit `/admin/` for admin panel

---

## 🎯 Learning Outcomes

This project helped in understanding:

* Django architecture (Project vs App)
* Models & ORM
* Authentication & session handling
* Forms and validation
* CRUD operations
* URL routing
* Template rendering

---

## 📌 Future Improvements

* 🔍 Search & filter books
* 📸 Add book cover images
* 📱 Improve UI with CSS/Bootstrap
* 🌍 Deploy online (Render / Railway / AWS)

---

## 👨‍💻 Author

*Atvee*

---

## 📄 Reference

Based on step-by-step implementation from: 

---

## ⭐ Final Note

This is a simple but complete Django project that demonstrates the **core fundamentals of web development**.

Perfect for beginners and a great starting point for building more advanced applications.
