import pick
from app.handle_tasks import add_task, edit_task, load_tasks


def add_or_edit_tasks():
    while True:
        tasks_list = load_tasks()
        options = tasks_list
        options.append("Add A Task")
        title = "Choose an option:"
        selected_option, index = pick.pick(options, title, indicator="=>")
        if selected_option == options[-1]:
            add_task(input("Enter A New Task: "))
        else:
            edited_task = input(f"Change {selected_option} To: ")
            edit_task(edited_task, index)
