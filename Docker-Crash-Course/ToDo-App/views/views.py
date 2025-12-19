# views/views.py
import os
from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__)
tasks_folder = 'tasks/'

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/view_tasks')
def view_tasks():
    tasks = load_tasks()
    return render_template('view_tasks.html', tasks=tasks)

@views.route('/create_task')
def create_task():
    return render_template('create_task.html')

@views.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form['description']
    save_task(title, description)
    return redirect(url_for('views.view_tasks'))

@views.route('/delete/<filename>')
def delete(filename):
    delete_task(filename)
    return redirect(url_for('views.view_tasks'))

@views.route('/mark_completed/<filename>')
def mark_completed(filename):
    # Placeholder for marking a task as completed
    return redirect(url_for('views.view_tasks'))

def load_tasks():
    tasks = []
    if not os.path.exists(tasks_folder):
        return tasks

    for filename in os.listdir(tasks_folder):
        filepath = os.path.join(tasks_folder, filename)
        with open(filepath, 'r') as file:
            task = {
                'title': filename[:-4],  # Remove the file extension
                'description': file.read(),
                'filename': filename
            }
            tasks.append(task)

    return tasks

def save_task(title, description):
    if not os.path.exists(tasks_folder):
        os.makedirs(tasks_folder)

    filename = f"{title}.txt"
    filepath = os.path.join(tasks_folder, filename)
    with open(filepath, 'w') as file:
        file.write(description)

def delete_task(filename):
    filepath = os.path.join(tasks_folder, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
