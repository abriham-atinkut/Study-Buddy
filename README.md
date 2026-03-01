# Study Buddy – Django REST API

**Study Buddy** is a web application built with **Django** and the **Django REST Framework (DRF)**. 

This project demonstrates a fully functional backend capable of managing data efficiently through a clean, scalable API while providing a built-in template system for easy interaction.

---

## 🚀 Key Features

* **Full CRUD Functionality**: Create, Read, Update, and Delete study rooms through API endpoints and the frontend.
* **Search Functionality**: Integrated search to help users find specific study rooms quickly.
* **Token-Based Authentication**: Secure access control ensuring only authorized users can modify data via Postman or other API clients.
* **Django Templates**: Includes a basic frontend to visualize database records directly in the browser.
* **Scalable Architecture**: Designed to serve as a robust backend for any modern frontend (React, Vue, etc.).



---

## 🛠 Tech Stack

* **Backend:** Python, Django
* **API Framework:** Django REST Framework (DRF)
* **Authentication:** TokenAuthentication
* **Tools:** Postman (for API testing & documentation)
* **Database:** SQLite (Default)

---

## 🔌 API Endpoints & Usage

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/api/token/` | Generate Auth Token | No |
| `GET` | `/rooms/` | List all rooms | **Yes** |
| `POST` | `/rooms/` | Create a new room | **Yes** |
| `PUT` | `/rooms/<id>/` | Update a room | **Yes** |
| `DELETE` | `/rooms/<id>/` | Delete a room | **Yes** |

### Authentication Workflow (Postman)
1.  **Access Denied**: Attempting to GET `/rooms/` without a token returns a 403 Forbidden error.
2.  **Token Generation**: Send `username` and `password` to the token endpoint to receive a unique key.
3.  **Authorized Access**: Add the token to the request header (`Authorization: Token <key>`) to unlock the full list of rooms.

---

## 💻 Installation & Setup

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-username/study-buddy.git](https://github.com/your-username/study-buddy.git)
   cd study-buddy

## Quick Setup

1. **Clone the repo**

```bash
git clone https://github.com/abriham-atinkut/Study-Buddy.git
cd Study-Buddy
```

2. **Set up a Virtual Environment**

Install virtualenv if you don't have it:

```bash
pip install virtualenv
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the development server**

```bash
python manage.py runserver
```
You can now view the app in you browser at:
```bash
http://127.0.0.1:8000/
```