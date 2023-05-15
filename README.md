# PyDo


This is a command-line To-Do List application written in Python. With this app, you can easily create, read, update, and delete tasks. The application uses a JSON file to store the tasks, which means that the tasks will persist even after you close the app.

**Features**
- Create tasks with a title, description, and due date.
- View all tasks or a specific task by ID.
- Update a task's title, description, or due date.
- Mark a task as completed.
- Delete a task by ID.
- Delete all tasks.

**Installation**
- Clone this repository: git clone https://github.com/officicalalkhaldi/PyDo.git
- Navigate to the project directory: cd PyDo
- python main.py -h for help

**Usage**
- To add a task: python main.py add "task title" "task description" "task due date (YYYY-MM-DD)"
- To view all tasks: python main.py show
- To view a specific task by ID: python main.py show <task_id>
- To update a task: python main.py update <task_id> "new task title" "new task description" "new task due date (YYYY-MM-DD)" (you can leave any field blank to keep the current value)
- To mark a task as completed: python main.py complete <task_id>
- To delete a task: python main.py delete <task_id>
- To delete all tasks: python main.py delete_all

**License**
- This project is licensed under the MIT License - see the LICENSE file for details.
