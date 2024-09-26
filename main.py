import functions
import time

print(f"Date: {time.strftime("%d-%m-%Y")} Time: {time.strftime("%H:%M:%S")}")
user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = functions.get_todos()
        todos.append(todo.capitalize())
        functions.store_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            index += 1
            row = f"{index}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            edit_number = int(user_action[5:]) - 1
            todos = functions.get_todos()
            new_todo = input("Enter a new todo: ")
            todos[edit_number] = new_todo.capitalize() + "\n"
            functions.store_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            complete_number = int(user_action[9:]) - 1
            todos = functions.get_todos()
            todo_to_remove = todos[complete_number]
            todos.pop(complete_number)
            functions.store_todos(todos)
            message = f"Todo '{todo_to_remove.strip("\n")}' was removed from the list."
            print(message)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("This item is not on the list.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Your command is not valid.")