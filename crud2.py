import os
class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_path = "tasks.txt"
        self.load_tasks_from_file()

    def save_tasks_to_file(self):
        try:
            with open(self.file_path, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task.id},{task.description}\n")
        except IOError as e:
            print(f"Error saving tasks to file: {e}")

    def load_tasks_from_file(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    for line in file:
                        id, description = line.strip().split(',')
                        self.tasks.append(Task(int(id), description))
            except IOError as e:
                print(f"Error loading tasks from file: {e}")

    def create_task(self, description):
        new_task_id = len(self.tasks) + 1
        new_task = Task(new_task_id, description)
        self.tasks.append(new_task)
        self.save_tasks_to_file()

    def read_tasks(self):
        for task in self.tasks:
            print(f"Task {task.id}: {task.description}")

    def update_task(self, task_id, new_description):
        for task in self.tasks:
            if task.id == task_id:
                task.description = new_description
                self.save_tasks_to_file()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks_to_file()


def main():
    task_manager = TaskManager()
    
    while True:
        print("\nTask Management Application")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            description = input("Enter task description: ").strip()
            task_manager.create_task(description)
        elif choice == '2':
            task_manager.read_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to update: ").strip())
            new_description = input("Enter new task description: ").strip()
            if not task_manager.update_task(task_id, new_description):
                print("Task not found.")
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: ").strip())
            task_manager.delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
