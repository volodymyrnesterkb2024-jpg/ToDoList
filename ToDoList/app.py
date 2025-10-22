from flask import Flask, render_template, request, redirect, url_for
from ToDoList.storage import load_tasks, save_tasks
from ToDoList.tasks import Task
from ToDoList.utils import find_task_by_id, get_next_id, get_priority_symbol

app = Flask(__name__)

@app.route('/')
def index():
    """Завантажує завдання та відображає їх у шаблоні."""
    tasks = load_tasks() 
  
    return render_template('index.html', tasks=tasks, get_priority_symbol=get_priority_symbol)


@app.route('/add', methods=['POST'])
def add():
    """Створює нове завдання на основі даних форми."""
    tasks = load_tasks()
    
    # Отримуємо дані з форми (input fields in index.html)
    title = request.form.get('title')
    priority = request.form.get('priority', 'medium')
    deadline = request.form.get('deadline') or None

    if title:

        new_id = get_next_id(tasks) 

        new_task = Task(id=new_id, title=title, priority=priority, deadline=deadline)
        
        tasks.append(new_task)
        save_tasks(tasks) 
    
    return redirect(url_for('index'))


@app.route('/complete/<int:id>')
def complete(id):
    """Змінює статус completed на протилежний."""
    tasks = load_tasks()
    task = find_task_by_id(tasks, id)
    
    if task:
        task.completed = not task.completed 
        save_tasks(tasks)
    
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    """Видаляє завдання зі списку."""
    tasks = load_tasks()

  
    new_tasks = [t for t in tasks if t.id != id]
    
    if len(new_tasks) < len(tasks): 
        save_tasks(new_tasks)
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    if not load_tasks():
        save_tasks([])
        
    app.run(debug=True)
