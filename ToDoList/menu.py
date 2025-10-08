from typing import List
from ToDoList.storage import save_tasks
from ToDoList.tasks import Task
from ToDoList.utils import find_task_by_id, get_next_id, validate_priority, get_int_input, get_priority_symbol

# Тут весь код menu.py без змін, крім імпортів
# show_tasks, add_task, complete_task, edit_task, delete_task, search_tasks, show_statistics
def show_tasks(tasks: List[Task], filter_type: str = "all"):
    """Показати завдання з можливістю фільтрації"""
    if not tasks:
        print("Список порожній.")
        return
    
    filtered_tasks = tasks
    if filter_type == "completed":
        filtered_tasks = [t for t in tasks if t.completed]
    elif filter_type == "active":
        filtered_tasks = [t for t in tasks if not t.completed]
    
    if not filtered_tasks:
        print(f"Немає завдань у категорії '{filter_type}'.")
        return
    
    print(f"\n{'='*60}")
    for task in filtered_tasks:
        status = "[X]" if task.completed else "[ ]"
        priority = get_priority_symbol(task.priority)
        deadline_str = f" | Дедлайн: {task.deadline}" if task.deadline else ""
        print(f"[{task.id}] {status} {priority} {task.title}{deadline_str}")
    print(f"{'='*60}\n")

def add_task(tasks: List[Task]):
    """Додати нове завдання"""
    title = input("Введіть назву завдання: ").strip()
    if not title:
        print("Назва не може бути порожньою!")
        return
    
    priority = input("Пріоритет (low/medium/high) [medium]: ").strip().lower() or "medium"
    if not validate_priority(priority):
        print("Невірний пріоритет, встановлено 'medium'")
        priority = "medium"
    
    deadline = input("Дедлайн (YYYY-MM-DD) [пропустити]: ").strip() or None
    
    new_id = get_next_id(tasks)
    new_task = Task(new_id, title, priority=priority, deadline=deadline)
    tasks.append(new_task)
    
    if save_tasks(tasks):
        print("Завдання додано!")

def complete_task(tasks: List[Task]):
    """Позначити завдання як виконане"""
    task_id = get_int_input("Введіть ID завдання для позначення виконаним: ")
    if task_id is None:
        return
    
    task = find_task_by_id(tasks, task_id)
    if task:
        task.completed = True
        if save_tasks(tasks):
            print("Завдання виконано!")
    else:
        print("Завдання не знайдено.")

def edit_task(tasks: List[Task]):
    """Редагувати завдання"""
    task_id = get_int_input("Введіть ID завдання для редагування: ")
    if task_id is None:
        return
    
    task = find_task_by_id(tasks, task_id)
    if not task:
        print("Завдання не знайдено.")
        return
    
    print(f"\nПоточна назва: {task.title}")
    new_title = input("Нова назва [пропустити]: ").strip()
    if new_title:
        task.title = new_title
    
    print(f"Поточний пріоритет: {task.priority}")
    new_priority = input("Новий пріоритет (low/medium/high) [пропустити]: ").strip().lower()
    if new_priority and validate_priority(new_priority):
        task.priority = new_priority
    
    print(f"Поточний дедлайн: {task.deadline or 'не встановлено'}")
    new_deadline = input("Новий дедлайн (YYYY-MM-DD) [пропустити]: ").strip()
    if new_deadline:
        task.deadline = new_deadline
    
    if save_tasks(tasks):
        print("Завдання оновлено!")

def delete_task(tasks: List[Task]) -> List[Task]:
    """Видалити завдання"""
    task_id = get_int_input("Введіть ID завдання для видалення: ")
    if task_id is None:
        return tasks
    
    task = find_task_by_id(tasks, task_id)
    if not task:
        print("Завдання не знайдено.")
        return tasks
    
    confirm = input(f"Видалити '{task.title}'? (y/n): ").strip().lower()
    if confirm == 'y':
        new_tasks = [t for t in tasks if t.id != task_id]
        if save_tasks(new_tasks):
            print("Завдання видалено!")
        return new_tasks
    else:
        print("Видалення скасовано.")
    return tasks

def search_tasks(tasks: List[Task]):
    """Пошук завдань за назвою"""
    query = input("Введіть текст для пошуку: ").strip().lower()
    if not query:
        print("Пошуковий запит не може бути порожнім!")
        return
    
    found = [t for t in tasks if query in t.title.lower()]
    if found:
        print(f"\nЗнайдено завдань: {len(found)}")
        show_tasks(found)
    else:
        print("Нічого не знайдено.")

def show_statistics(tasks: List[Task]):
    """Показати статистику"""
    if not tasks:
        print("Немає завдань для статистики.")
        return
    
    total = len(tasks)
    completed = sum(1 for t in tasks if t.completed)
    active = total - completed
    
    print(f"\n{'='*40}")
    print(f"СТАТИСТИКА")
    print(f"{'='*40}")
    print(f"Всього завдань: {total}")
    print(f"Виконано: {completed} ({completed/total*100:.1f}%)")
    print(f"Активних: {active} ({active/total*100:.1f}%)")
    print(f"{'='*40}\n")