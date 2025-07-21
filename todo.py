# todo.py
todos = []

def add(todo_item):
    """Add a task to the to-do list"""
    todos.append(todo_item)

    def clear():
        """Clear all the task from the to-do list"""
        todos.clear()

        def get_todos():
            return todos