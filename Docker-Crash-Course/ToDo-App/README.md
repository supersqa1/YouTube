# Simple TODO App Built With Flask

A demo Flask application that demonstrates proper Python project setup and management.

This demo shows:
 * How to set up Python virtual environments
 * How to manage dependencies with requirements.txt
 * How to run a Flask application locally

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup and Installation

### 1. Clone or Download the Repository

```bash
cd todo-app-flask-demo
```

### 2. Create a Virtual Environment

#### On Mac/Linux:
```bash
python3 -m venv venv
```

#### On Windows:
```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### On Mac/Linux:
```bash
source venv/bin/activate
```

#### On Windows (Command Prompt):
```bash
venv\Scripts\activate
```

#### On Windows (PowerShell):
```bash
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

The app will start running on `http://localhost:5151`

Open your web browser and navigate to `http://localhost:5151` to use the app.

## Usage

- **Home**: Landing page with navigation
- **View Tasks**: See all your tasks and their statuses
- **Create Task**: Add new tasks with title and description
- **Update Status**: Mark tasks as todo, in progress, or done
- **Delete Task**: Remove completed or unwanted tasks

## Deactivating the Virtual Environment

When you're done working with the app, you can deactivate the virtual environment:

```bash
deactivate
```

## Troubleshooting

- **Port already in use**: If port 5151 is already in use, you can modify the port in `app.py` (line 84)
- **Permission denied on Windows PowerShell**: You may need to run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` before activating the virtual environment