def main():
    # print(load_tasks())
    print(load_tasks())


# load the tasks and return them as a list
def load_tasks():
    with open("tasks.txt", "r") as f:
        tasks_list = f.read().split("\n")
        if tasks_list[-1] == "":
            tasks_list.pop()
        return tasks_list


# add a task to the end of the list
def add_task(task):
    with open("tasks.txt", "a") as f:
        f.write(f"{task}\n")


# Get a task name and change the old task with it
def edit_task(new_task_name, line_number):
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    if 0 <= line_number < len(lines):
        lines[line_number] = new_task_name + "\n"
    with open("tasks.txt", "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
