import pick
import time

from app.handle_tasks import load_tasks


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
    options = load_tasks()
    title = "Choose an option:"
    selected_option, index = pick.pick(options, title, indicator="=>")
    return selected_option


def start_session(duration, task):
    print(task)
    if duration > 0:

        print("Press space bar to pause")
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
