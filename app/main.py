import pick

from app.add_or_edit_tasks import add_or_edit_tasks
from app.start_a_new_session import new_session_choice

# from handle_tasks import add_task, edit_task, load_tasks


def select_options(options_list, title):
    selected_option, index = pick.pick(options_list, title, indicator="=>")
    return selected_option, index


def main():

    # start_session(int(input("Enter The Session Time (In Minutes): ")))
    while True:
        options = ["Start A New Session", "Add/Edit Task", "Stats", "Exit"]
        title = "Choose an option:"
        selected_option, index = select_options(options, title)

        if selected_option == options[0]:
            new_session_choice()

        if selected_option == options[1]:
            add_or_edit_tasks()
            break


if __name__ == "__main__":
    main()
