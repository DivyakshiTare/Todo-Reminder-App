# To-Do List Application

A simple To-Do List application with a **HTML, CSS, Javascript Frontend**, a **Flask backend**, and **PostgreSQL** as the database.

---

## Features

- Add a new To-Do Task
- Display list of To-Do Tasks
- Edit or delete a particular To-Do Task
- Delete all To-Do Tasks

---

## Project Structure

    TODO-LIST/
    ├── app/
    │   ├── __pycache__/
    │   ├── templates/
    │   │   └── index.html
    │   ├── __init__.py
    │   ├── config.py
    │   ├── models.py
    │   └── routes.py
    ├── env/
    ├── static/
    ├── tests/
    │   ├── __pycache__/
    │   ├── __init__.py
    │   ├── conftest.py
    │   └── test_api.py
    ├── .env
    ├── requirements.txt
    └── run.py



---

## Tech Stack

- **Frontend**: HTML, CSS, Javascript
- **Backend**: Flask (Python)
- **Database**: Postgresql

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DivyakshiTare/Todo-Reminder-App.git
cd TODO-LIST
```

### 2. Create Databases in Postgresql

   ```bash
   CREATE DATABASE todo_db;
   CREATE DATABASE todo_test_db;
   ```


### 3. In Terminal 1

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with following content:

   ```env
   DATABASE_URL=postgresql://database_user:database_password@localhost:5432/todo_db
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=2025
   ```

### 4. In Terminal 2

1. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
2. Run the Flask server:

   ```bash
   python run.py
   ```


### 5. To run tests (in either terminal with virtual environment activated)

1. Run tests with coverage report:

   ```bash  
   pytest --cov=app tests/
   ```

2.  Run specific test file:

   ```bash
   pytest tests/test_api.py -v
   ```

---


### Endpoints

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| GET    | `/tasks`           | Fetch all tasks     |
| POST   | `/tasks`           | Create a new task   |
| PUT    | `/tasks/<task_id>` | Update a task by ID |
| DELETE | `/tasks/<task_id>` | Delete a task by ID |
| DELETE | `/tasks`           | Delete all tasks    |

---

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

---
