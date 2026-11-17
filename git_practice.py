"""
Git Practice File
=================

Use this file to practise Git commands without worrying about breaking a real project.

Suggested exercises:
1. Save this file, then run: git status
2. Stage and commit it.
3. Change the greeting below, then create another commit.
4. Create a branch and add a new task.
5. Switch back to main and make a different change.
6. Merge your branch.
7. Practise a merge conflict by editing the same line on two branches.

Run it with:
    python git_practice.py
"""

tasks = [
    {"id": 1, "title": "Learn git status", "completed": False},
    {"id": 2, "title": "Practise git add and commit", "completed": False},
]


def show_greeting():
    # GIT EXERCISE: Change this message and commit your change.
    print("Hello! I am practising Git.")


def show_tasks():
    print("\nMy practice tasks:")
    for task in tasks:
        status = "Done" if task["completed"] else "Not done"
        print(f'{task["id"]}. {task["title"]} — {status}')


def add_task(title):
    """Add a new task to the in-memory task list."""
    new_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({"id": new_id, "title": title, "completed": False})
    print(f'Added task: {title}')


def complete_task(task_id):
    """Mark a task as completed."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(f'Completed task: {task["title"]}')
            return
    print(f"No task found with ID {task_id}.")


def main():
    show_greeting()
    show_tasks()

    # GIT EXERCISE: Add your own task here, then commit the change.
    add_task("Practise creating a Git branch")

    # GIT EXERCISE: Try changing 1 to 2, then run the file again.
    complete_task(1)

    show_tasks()


if __name__ == "__main__":
    main()
