from datetime import datetime

def show_menu():
    print(
    """===== ПЕРСОНАЛЬНИЙ МЕНЕДЖЕР ЗАВДАНЬ =====
    1. Додати завдання
    2. Переглянути всі завдання
    3. Знайти завдання
    4. Редагувати завдання
    5. Змінити статус завдання
    6. Видалити завдання
    7. Фільтрувати завдання
    8. Сортувати завдання
    9. Показати статистику
    10. Показати пріоритетні завдання
    0. Вийти з програми""")
    pass

def add_task(tasks):
    print("Додати завдання. Введіть наступні дані для нового завдання:")
    while True:
        try:
            task_name = input("Назва завдання: ").strip()
            if not task_name:
                raise ValueError("Назва завдання не може бути порожньою. Будь ласка, введіть назву завдання.")
            if len(task_name) > 128:
                raise ValueError("Назва завдання не може перевищувати 128 символів. Будь ласка, введіть коротшу назву завдання.")
            if (task_name.casefold() in [task['task_name'].casefold() for task in tasks]):
                raise ValueError("Завдання з такою назвою вже існує. Будь ласка, введіть унікальну назву завдання.")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            category = input("Категорія: ").strip()
            if not category:
                raise ValueError("Категорія не може бути порожньою. Будь ласка, введіть категорію.")
            if len(category) > 128:
                raise ValueError("Категорія не може перевищувати 128 символів. Будь ласка, введіть коротшу категорію.")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
            try:
                description = input("Короткий опис: ").strip()
                if not description:
                    raise ValueError("Короткий опис не може бути порожнім. Будь ласка, введіть короткий опис.")
                if len(description) > 256:
                    raise ValueError("Короткий опис не може перевищувати 256 символів. Будь ласка, введіть коротший опис.")
            except ValueError as e:
                print(e)
            else:
                break

    while True:
        try:
            priority = int(input("""Пріоритет (1-3):
            1. Високий
            2. Середній
            3. Низький
            """).strip())
            if priority not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Невірний пріоритет. Будь ласка, введіть число від 1 до 3.")
        else:
            break

    while True:
        deadline_text = input("Термін виконання (ДД.ММ.РРРР): ").strip()
        if not deadline_text:
            print("Термін виконання не може бути порожнім.")
            continue
        try:
            deadline = datetime.strptime(deadline_text, "%d.%m.%Y").date()
        except ValueError:
            print("Введіть коректну дату у форматі ДД.ММ.РРРР.")
        else:
            break
    
    return {
        "task_name": task_name,
        "category": category,
        "description": description,
        "priority": priority,
        "deadline": deadline,
        "status": "Нове"
    }

def show_tasks():
    pass

def search_tasks():
    pass

def edit_task():
    pass

def change_status():
    pass

def delete_task():
    pass

def filter_tasks():
    pass

def sort_tasks():
    pass

def show_statistics():
    pass

def show_priority_tasks():
    pass

tasks = []
while True:
    show_menu();
    choice = input("Виберіть дію (0-10): ").strip()
    match choice:
        case "1":
            task = add_task(tasks)
            tasks.append(task)
            print("Завдання додано успішно!")
            print(tasks)
        case "2":
            show_tasks()
        case "3":
            search_tasks()
        case "4":
            edit_task()
        case "5":
            change_status()
        case "6":
            delete_task()
        case "7":
            filter_tasks()
        case "8":
            sort_tasks()
        case "9":
            show_statistics()
        case "10":
            show_priority_tasks()
        case "0":
            print("Вийти з програми")
            break
        case _:
            print("Невірний вибір. Спробуйте ще раз.")