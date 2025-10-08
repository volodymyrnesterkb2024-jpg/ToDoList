import json
import os
from typing import List
from ToDoList.tasks import Task

FILE_NAME = "tasks.json"

def load_tasks() -> List[Task]:
    """Завантажити завдання з файлу"""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Task(**task) for task in data]
    except (json.JSONDecodeError, IOError) as e:
        print(f"Помилка читання файлу: {e}")
        return []

def save_tasks(tasks: List[Task]) -> bool:
    """Зберегти завдання у файл"""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump([task.__dict__ for task in tasks], f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Помилка запису файлу: {e}")
        return False
