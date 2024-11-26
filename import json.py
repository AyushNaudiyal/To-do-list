import json
from datetime import datetime, date

class TodoList:
    def __init__(self, filename='todos.json'):
        """Initialize the TodoList with a JSON file for persistence"""
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        """Load todos from JSON file or return empty list"""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.todos, file, indent=4)

    def add_todo(self, title, description='', priority='medium', due_date=None):
        """Add a new todo item"""
        todo = {
            'id': len(self.todos) + 1,
            'title': title,
            'description': description,
            'priority': priority,
            'completed': False,
            'created_at': str(datetime.now()),
            'due_date': str(due_date) if due_date else None
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"Todo '{title}' added successfully!")

    def list_todos(self, filter_type=None):
        """List todos with optional filtering"""
        if not self.todos:
            print("No todos found.")
            return

        filtered_todos = self.todos
        if filter_type == 'completed':
            filtered_todos = [todo for todo in self.todos if todo['completed']]
        elif filter_type == 'pending':
            filtered_todos = [todo for todo in self.todos if not todo['completed']]

        for todo in sorted(filtered_todos, key=lambda x: x.get('priority', 'medium')):
            status = '✓' if todo['completed'] else ' '
            print(f"[{status}] ID: {todo['id']} | Title: {todo['title']} "
                  f"| Priority: {todo['priority']} "
                  f"| Due: {todo.get('due_date', 'No due date')}")

    def update_todo(self, todo_id, **kwargs):
        """Update an existing todo item"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo.update(kwargs)
                self.save_todos()
                print(f"Todo {todo_id} updated successfully!")
                return
        print(f"Todo with ID {todo_id} not found.")

    def complete_todo(self, todo_id):
        """Mark a todo as completed"""
        self.update_todo(todo_id, completed=True)

    def delete_todo(self, todo_id):
        """Delete a todo item"""
        self.todos = [todo for todo in self.todos if todo['id'] != todo_id]
        self.save_todos()
        print(f"Todo {todo_id} deleted successfully!")

def main_menu():
    """Display main menu and handle user interactions"""
    todo_list = TodoList()

    while True:
        print("\n--- Python Todo List ---")
        print("1. Add Todo")
        print("2. List All Todos")
        print("3. List Completed Todos")
        print("4. List Pending Todos")
        print("5. Update Todo")
        print("6. Complete Todo")
        print("7. Delete Todo")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        try:
            if choice == '1':
                title = input("Enter todo title: ")
                description = input("Enter description (optional): ")
                priority = input("Enter priority (low/medium/high, default medium): ") or 'medium'
                todo_list.add_todo(title, description, priority)

            elif choice == '2':
                todo_list.list_todos()

            elif choice == '3':
                todo_list.list_todos('completed')

            elif choice == '4':
                todo_list.list_todos('pending')

            elif choice == '5':
                todo_id = int(input("Enter todo ID to update: "))
                title = input("Enter new title (press enter to skip): ")
                description = input("Enter new description (press enter to skip): ")
                priority = input("Enter new priority (press enter to skip): ")

                update_data = {}
                if title: update_data['title'] = title
                if description: update_data['description'] = description
                if priority: update_data['priority'] = priority

                todo_list.update_todo(todo_id, **update_data)

            elif choice == '6':
                todo_id = int(input("Enter todo ID to complete: "))
                todo_list.complete_todo(todo_id)

            elif choice == '7':
                todo_id = int(input("Enter todo ID to delete: "))
                todo_list.delete_todo(todo_id)

            elif choice == '8':
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_menu()