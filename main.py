import argparse
from json import JSONDecodeError, dumps, dump, loads
import logging
from os.path import exists

class Controller:
    def __init__(self, fname: str = "tasks.json"):
        self.fname = fname
        self.path = "./" + self.fname
        self.tasks = []
        self.check_file()

    def check_file(self):
        if not exists(self.path):
            with open(self.path, "w") as f:
                f.write(dumps([]))

    def get_all(self):
        try:
            with open(self.path, "r") as f:
                self.tasks = loads(f.read())
                print(dumps(self.tasks, indent=4))
        except (FileNotFoundError, JSONDecodeError):
            self.tasks = []

    def add_task(self, task: dict):
        with open(self.path, "r+") as f:
            self.tasks = loads(f.read())
            max_id = max(task["id"] for task in self.tasks) if self.tasks else 0
            new_task_id = max_id + 1
            if task not in self.tasks:
                task["id"] = new_task_id
                self.tasks.append(task)
                f.seek(0)
                dump(self.tasks, f)
                print("Task added successfully.")
            else:
                print("Task already exists.")

    def update_task(self, iid: int, new_task: dict):
        with open(self.fname, 'r') as f:
            tasks = loads(f.read())
    

        for task in tasks:
            if task['id'] == iid:
                task.update(new_task)
                break
    
        with open(self.fname, 'w') as f:
            dump(tasks, f, indent=4)
        
        print("Task updated successfully.")

    def delete_task(self, task_id):
        with open(self.path, "r") as f:
            tasks = loads(f.read())
            ids = [i["id"] for i in tasks]
            if task_id not in ids:
                print("Task with ID", task_id, "not found.")
            else:
                for i, task in enumerate(tasks):
                    if int(task["id"]) == int(task_id):
                        del tasks[i]
                        break

        with open(self.path, "w") as f:
            dump(tasks, f)
        
    def delete_all(self):
        with open(controller.path, "w") as f:
            f.write(dumps([]))
            print("All tasks deleted successfully.")
    

    def show_info(self):
        """Display the content of the log file"""
        with open("logs.txt", 'r') as f:
            content = f.read()
            print(content)



class Logger:
    def __init__(self, filename: str = "log.txt", level: int = logging.INFO, quiet: bool = False):
        self.filename = filename
        self.level = level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.level)
        
        self.file_handler = logging.FileHandler(self.filename)
        self.file_handler.setLevel(self.level)

        if not quiet:
            self.stream_handler = logging.StreamHandler()
            self.stream_handler.setLevel(self.level)

            self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            self.file_handler.setFormatter(self.formatter)
            self.stream_handler.setFormatter(self.formatter)

            self.logger.addHandler(self.file_handler)
            self.logger.addHandler(self.stream_handler)
        else:
            self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            self.file_handler.setFormatter(self.formatter)
            self.logger.addHandler(self.file_handler)

    def log(self, message: str):
        self.logger.info(message)




class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Task Manager')

        self.parser.add_argument('action', type=str, help='Action to perform', choices=['show', 'info', 'add', 'update', 'delete', "delete_all"])
        self.parser.add_argument('task_id', type=int, nargs='?', help='ID of task to modify')

        self.parser.add_argument('--title', type=str, help='Name of new task to add')
        self.parser.add_argument('--desc', type=str, help='Description of new task to add')
        self.parser.add_argument('--status', type=str, help='Description of new task to add')

    def parse_args(self):
        return self.parser.parse_args()




if __name__ == '__main__':
    logger = Logger("logs.txt", quiet=True)
    logger.log("Starting task manager...")

    arg_parser = Parser()
    args = arg_parser.parse_args()

    controller = Controller("tasks.json")
    controller.check_file()

    if args.action == "show":
        logger.log("Getting all tasks...")
        controller.get_all()

    elif args.action == "add":
        logger.log("Adding new task...")
        task = {"id": len(controller.tasks) + 1, "task": args.title, "description": args.desc, "status": args.status}
        controller.add_task(task)

    elif args.action == "update":
        logger.log("Updating task...")
        task = {"id": args.task_id, "task": args.title, "description": args.desc, "status": args.status}
        controller.update_task(args.task_id, task)

    elif args.action == "delete":
        logger.log("Deleting task...")
        controller.delete_task(args.task_id)

    elif args.action == "delete_all":
        logger.log("Deleting all tasks...")
        controller.delete_all()
    
    if args.action == 'info':
        controller.show_info()