import pick
import time

from handle_tasks import add_task, edit_task, load_tasks


# get a time in minutes and convert it to seconds if the minutes are greater than 0 or it will produce and error
def convert_minutes_to_seconds(minutes: int) -> int:
    """
    Dummy function: converts minutes to seconds.
    """
    if minutes < 0:
        raise ValueError("Time cannot be negative")
    return minutes * 60


def select_options():
    pass


# It will ask the use either he want to set a specific duration or wanna do an open time session
def new_session_choice():
    options = ["Set Session Duration", "Free Time"]
    title = "Choose an option:"
    selected_option, index = pick.pick(options, title, indicator="=>")
    if selected_option == options[0]:
        task = choose_task()
        start_session((int(input("Enter The Session Time (In Minutes): ")) * 60), task)
    elif selected_option == options[1]:
        task = choose_task()
        start_session(0, task)


# Get a task choise and return it
def choose_task():
    options = ["Reading Quran", "Coding", "Random"]
    title = "Choose an option:"
    selected_option, index = pick.pick(options, title, indicator="=>")
    return selected_option


# A countdown that will the take the time in seconds and display it


def start_session(duration, task):
    print(task)
    if duration > 0:
        while duration:
            mins, secs = divmod(duration, 60)
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            duration -= 1
    else:
        while True:
            mins, secs = divmod(duration, 60)
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            duration += 1


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


def main():

    # start_session(int(input("Enter The Session Time (In Minutes): ")))
    while True:
        options = ["Start A New Session", "Add/Edit Task", "Stats", "Exit"]
        title = "Choose an option:"
        selected_option, index = pick.pick(options, title, indicator="=>")

        if selected_option == options[0]:
            new_session_choice()

        if selected_option == options[1]:
            add_or_edit_tasks()
            break


if __name__ == "__main__":
    main()
