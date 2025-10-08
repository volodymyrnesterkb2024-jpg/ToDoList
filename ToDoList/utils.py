from typing import List, Optional
from ToDoList.tasks import Task

def find_task_by_id(tasks: List[Task], task_id: int) -> Optional[Task]:
    """Знайти завдання за ID"""
    return next((task for task in tasks if task.id == task_id), None)

def get_next_id(tasks: List[Task]) -> int:
    """Отримати наступний доступний ID"""
    return max([task.id for task in tasks], default=0) + 1

def validate_priority(priority: str) -> bool:
    """Перевірити валідність пріоритету"""
    return priority.lower() in ["low", "medium", "high"]

def get_int_input(prompt: str) -> Optional[int]:
    """Отримати числове значення від користувача"""
    try:
        return int(input(prompt))
    except ValueError:
        print("Потрібно ввести число!")
        return None

def get_priority_symbol(priority: str) -> str:
    """Отримати символ для пріоритету"""
    symbol_map = {
        "low": "[L]",
        "medium": "[M]",
        "high": "[H]"
    }
    return symbol_map.get(priority.lower(), "[ ]")
