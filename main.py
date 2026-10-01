from datetime import datetime

def show_menu():
    print(
    """\n===== ПЕРСОНАЛЬНИЙ МЕНЕДЖЕР ЗАВДАНЬ =====
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

def input_task_data(tasks, current_task=None):
    if current_task is None:
        current_task = {}
    while True:
        try:
            task_name = input("Назва завдання: ").strip() or current_task.get("task_name", "")
            if not task_name:
                raise ValueError("Назва завдання не може бути порожньою. Будь ласка, введіть назву завдання.")
            if len(task_name) > 128:
                raise ValueError("Назва завдання не може перевищувати 128 символів. Будь ласка, введіть коротшу назву завдання.")
            if task_name.casefold() in [task['task_name'].casefold() for task in tasks if task is not current_task]:
                raise ValueError("Завдання з такою назвою вже існує. Будь ласка, введіть унікальну назву завдання.")
        except ValueError as e:
            print(e)
        else:
            break

    while True:
        try:
            category = input("Категорія: ").strip() or current_task.get("category", "")
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
            description = input("Короткий опис: ").strip() or current_task.get("description", "")
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
            """).strip() or current_task.get("priority", ""))
            if priority not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Невірний пріоритет. Будь ласка, введіть число від 1 до 3.")
        else:
            break

    while True:
        deadline_text = input("Термін виконання (ДД.ММ.РРРР): ").strip()
        if not deadline_text and current_task:
            deadline = current_task["deadline"]
            break
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
    }


def add_task(tasks):
    print("Додати завдання. Введіть наступні дані для нового завдання:")
    task = input_task_data(tasks)
    task["task_id"] = max((t["task_id"] for t in tasks), default=0) + 1
    task["status"] = "нове"
    return task

def show_tasks(tasks):
    print("===== СПИСОК ЗАВДАНЬ =====\n")
    if tasks == []:
        print("Список завдань порожній. Виконайте команду \"1\", щоб додати завдання.")
    else:
        for task in tasks:
            print( f"{task['task_id']}. Назва: {task['task_name']}", f"Категорія: {task['category']}", f"Опис: {task['description']}", f"Пріоритет: {task['priority']}", f"Термін виконання: {task['deadline'].strftime('%d.%m.%Y')}", f"Статус: {task['status']}" + "\n", sep="\n")
    pass

def search_tasks(tasks):
    query = input("Введіть слово або частину слова для пошуку(0 - повернутися до меню): ").strip()
    if query == "0":
        return
    result = [
        task for task in tasks
        if any(query.casefold() in str(value).casefold() for value in task.values())
    ]
    if result:
        for task in result:
            print( f"{task['task_id']}. Назва: {task['task_name']}", f"Категорія: {task['category']}", f"Опис: {task['description']}", f"Пріоритет: {task['priority']}", f"Термін виконання: {task['deadline'].strftime('%d.%m.%Y')}", f"Статус: {task['status']}" + "\n", sep="\n")
    else:
        print("Завдання не знайдено.")

    pass

def edit_task(tasks):
    while True:
        raw_input = input("Введіть номер завдання для редагування (0 - повернутися до меню): ").strip()
        if raw_input == "0":
            return
        try:
            task_id = int(raw_input)
            break
        except ValueError:
            print("Помилка: номер завдання має бути цілим числом. Спробуйте ще раз.")
    task = next((t for t in tasks if t["task_id"] == task_id), None)
    if not task:
        print("Завдання з таким номером не знайдено.")
        return

    print(f"Редагування завдання: {task['task_name']}")
    print("Залиште поле порожнім, щоб не змінювати його.")
    task.update(input_task_data(tasks, task))

    print("Завдання успішно відредаговано.")

def change_status(tasks):
    if not tasks:
        print("Список завдань порожній.")
        return

    show_tasks(tasks)
    while True:
        raw_input = input("Введіть номер завдання для зміни статусу (0 - повернутися до меню): ").strip()
        if raw_input == "0":
            return
        try:
            task_id = int(raw_input)
            break
        except ValueError:
            print("Помилка: номер завдання має бути цілим числом. Спробуйте ще раз.")

    task = next((t for t in tasks if t["task_id"] == task_id), None)
    if task is None:
        print("Завдання з таким номером не знайдено.")
        return

    print(f"Поточний статус завдання: {task['status']}")
    statuses = {"1": "нове", "2": "у роботі", "3": "виконане"}
    while True:
        choice = input("""Оберіть новий статус (0 - повернутися до меню):
        1. нове
        2. у роботі
        3. виконане
        """).strip()
        if choice == "0":
            return
        if choice in statuses:
            task["status"] = statuses[choice]
            print("Статус завдання успішно змінено.")
            return
        print("Невірний статус. Будь ласка, введіть число від 1 до 3.")

def delete_task(tasks):
    if not tasks:
        print("Список завдань порожній.")
        return

    show_tasks(tasks)
    while True:
        raw_input = input("Введіть номер завдання для видалення (0 - повернутися до меню): ").strip()
        if raw_input == "0":
            return
        try:
            task_id = int(raw_input)
            break
        except ValueError:
            print("Помилка: номер завдання має бути цілим числом. Спробуйте ще раз.")

    task = next((t for t in tasks if t["task_id"] == task_id), None)
    if task is None:
        print("Завдання з таким номером не знайдено.")
        return

    print("Вибране завдання для видалення:")
    show_tasks([task])
    confirmation = input("Видалити це завдання? (так/ні): ").strip().lower()
    if confirmation == "так":
        tasks.remove(task)
        print("Завдання успішно видалено.")
    else:
        print("Видалення скасовано.")

def filter_tasks(tasks):
    if not tasks:
        print("Список завдань порожній.")
        return

    choice = input("""Оберіть критерій фільтрації (0 - повернутися до меню):
    1. Категорія
    2. Статус
    3. Пріоритет
    """).strip()
    if choice == "0":
        return

    if choice == "1":
        category = input("Введіть категорію: ").strip()
        if not category:
            print("Категорія не може бути порожньою.")
            return
        result = [task for task in tasks if task["category"].casefold() == category.casefold()]
    elif choice == "2":
        status = input("""Оберіть статус (0 - повернутися до меню):
        1. нове
        2. у роботі
        3. виконане
        4. усі невиконані
        """).strip()
        if status == "0":
            return
        statuses = {"1": "нове", "2": "у роботі", "3": "виконане"}
        if status == "4":
            result = [task for task in tasks if task["status"] != "виконане"]
        elif status in statuses:
            result = [task for task in tasks if task["status"] == statuses[status]]
        else:
            print("Невірний статус. Будь ласка, введіть число від 1 до 4.")
            return
    elif choice == "3":
        priority = input("""Оберіть пріоритет (0 - повернутися до меню):
        1. Високий
        2. Середній
        3. Низький
        """).strip()
        if priority == "0":
            return
        if priority not in ["1", "2", "3"]:
            print("Невірний пріоритет. Будь ласка, введіть число від 1 до 3.")
            return
        result = [task for task in tasks if task["priority"] == int(priority)]
    else:
        print("Невірний критерій фільтрації.")
        return

    print("===== РЕЗУЛЬТАТ ФІЛЬТРАЦІЇ =====")
    if result:
        show_tasks(result)
    else:
        print("Завдання за обраним критерієм не знайдено.")

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
        case "2":
            show_tasks(tasks)
        case "3":
            search_tasks(tasks)
        case "4":
            show_tasks(tasks)
            edit_task(tasks)
        case "5":
            change_status(tasks)
        case "6":
            delete_task(tasks)
        case "7":
            filter_tasks(tasks)
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
