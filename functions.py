filepath_1 = ("/Users/yannick/Library/CloudStorage/OneDrive-Persoonlijk/ISSO/Courses/Python zelfstudie/"
              "Python_Mega_Course_60_Days/App 1/pythonProject/todos.txt")


def get_todos():
    """Read a text file and return the to-do items."""
    with open(filepath_1, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def store_todos(todos_arg):
    """Take a to-do list and store them in a text file."""
    with open(filepath_1, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")