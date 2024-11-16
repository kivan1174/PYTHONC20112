from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Виконано" if self.is_completed else "Не виконано"
        deadline_str = self.deadline.strftime("%Y-%m-%d")
        return f"[{status}] {self.title} (до {deadline_str}) - {self.description}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        task = Task(title, description, deadline)
        self.tasks.append(task)
        print(f"Завдання '{title}' додано")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Завдання '{title}' видалено")
                return
        print(f"Завдання '{title}' не знайдено")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                print(f"Завдання '{title}' відмічено як виконане")
                return
        print(f"Завдання '{title}' не найдено")

    def list_tasks(self):
        if not self.tasks:
            print("Список завдань пустий.")
        else:
            print("Список завдань:")
            for task in self.tasks:
                print(task)



if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Прочитати книгу", "Закінчити читання книжки до наступного тижня", "2024-11-17")
    manager.add_task("Купити продукти", "Купити хлеб", "2024-11-17")
    manager.list_tasks()
    manager.mark_task_completed("Купити продукти")
    manager.list_tasks()
    manager.remove_task("Прочитати книгу")
    manager.list_tasks()