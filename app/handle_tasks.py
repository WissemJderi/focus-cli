def main():
    # print(load_tasks())
    add_task()
    print(load_tasks())


# load the tasks and return them as a list
def load_tasks():
    with open("tasks.txt") as f:
        return f.read().split("\n")


# add a task to the end of the list
def add_task():
    with open("tasks.txt", "a") as f:
        f.write("Planning")


if __name__ == "__main__":
    main()
