

### `README.md`

# Python Todo List Application

A simple Python-based Todo List application that lets you manage your tasks efficiently. The application uses a JSON file for data persistence and provides features like adding, updating, completing, and deleting tasks.

---

## Features

- **Add Todos:** Create tasks with a title, description, priority, and optional due date.
- **List Todos:** View all tasks, filter by completed or pending status.
- **Update Todos:** Modify task details, such as title, description, and priority.
- **Complete Todos:** Mark tasks as completed.
- **Delete Todos:** Remove tasks permanently.
- **Persistent Storage:** Todos are saved in a `todos.json` file for reuse.

---

## Prerequisites

- Python 3.6 or higher
- Basic knowledge of Python to run the script

---

## Installation

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/your-username/todo-list-app.git
   cd todo-list-app
   ```

2. Ensure Python is installed. Check the version with:
   ```bash
   python --version
   ```

3. No additional libraries are required. The program uses Python's standard library.

---

## Usage

1. Run the program:
   ```bash
   python todo_list.py
   ```

2. Follow the menu options displayed to interact with the Todo List:
   - **Add Todo:** Enter details like title, description, and priority.
   - **List Todos:** View all tasks with their status, ID, and priority.
   - **Update Todo:** Modify an existing task by its ID.
   - **Complete Todo:** Mark a task as completed.
   - **Delete Todo:** Remove a task from the list.

3. Exit the program when done, and all your tasks will be saved in `todos.json`.

---

## Menu Options

| Option | Description                          |
|--------|--------------------------------------|
| 1      | Add a new todo item                 |
| 2      | List all todos                      |
| 3      | List completed todos                |
| 4      | List pending todos                  |
| 5      | Update an existing todo             |
| 6      | Mark a todo as completed            |
| 7      | Delete a todo                       |
| 8      | Exit the program                    |

---

## Data Storage

The application stores todos in a file named `todos.json` in the same directory as the script. This ensures all tasks persist between program executions.

---

## Example

### Adding a Todo
```
Enter todo title: Buy groceries
Enter description (optional): Milk, eggs, bread
Enter priority (low/medium/high, default medium): high
Todo 'Buy groceries' added successfully!
```

### Listing Todos
```
--- Python Todo List ---
[ ] ID: 1 | Title: Buy groceries | Priority: high | Due: No due date
```

---

## Known Limitations

- **Concurrent Usage:** The application isn't designed for multiple users or concurrent sessions.
- **Due Date Validation:** Dates are stored as strings and not validated.

---


---

Feel free to enhance the functionality or adapt the code for your needs. Happy coding! 😊
