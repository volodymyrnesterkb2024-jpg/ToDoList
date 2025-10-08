from ToDoList.storage import load_tasks
from ToDoList.menu import (show_tasks, add_task, complete_task, edit_task, 
                           delete_task, search_tasks, show_statistics)

def main():
    """Головна функція програми"""
    tasks = load_tasks()
    
    while True:
        print("\n" + "="*50)
        print("TO-DO LIST MANAGER")
        print("="*50)
        print("1. Показати всі завдання")
        print("2. Показати виконані")
        print("3. Показати активні")
        print("4. Додати завдання")
        print("5. Позначити виконаним")
        print("6. Редагувати завдання")
        print("7. Видалити завдання")
        print("8. Пошук завдань")
        print("9. Статистика")
        print("0. Вихід")
        print("="*50)

        choice = input("Оберіть дію: ").strip()
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            show_tasks(tasks, "completed")
        elif choice == "3":
            show_tasks(tasks, "active")
        elif choice == "4":
            add_task(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            edit_task(tasks)
        elif choice == "7":
            tasks = delete_task(tasks)
        elif choice == "8":
            search_tasks(tasks)
        elif choice == "9":
            show_statistics(tasks)
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()