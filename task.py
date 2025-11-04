import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler for WARNING and above
file_handler = logging.FileHandler('todo_log.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - Line %(lineno)d - %(message)s')
file_handler.setFormatter(file_formatter)

# Console handler for INFO and above
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s - Line %(lineno)d - %(message)s')
console_handler.setFormatter(console_formatter)

# Add handlers to logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def to_do_list(listo: list = None) -> None:
    if listo is None:
        listo = []

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        print("=" * 50)
        x: str = input("Enter your choice: ")
        logger.info(f"User selected option: {x}")

        if x == "1":
            tsk = input("Enter task: ")
            listo.append(tsk)
            logger.info(f"Task added: {tsk}")
            print("-" * 50)

        elif x == "2":
            print("Tasks:")
            for i, t in enumerate(listo):
                print(f"{i+1}. {t}")
            logger.info("Displayed task list.")
            print("-" * 50)

        elif x == "3":
            usr_input: str = input("Enter task number to mark as done: ")
            try:
                index = int(usr_input) - 1
                if 0 <= index < len(listo):
                    removed_task = listo.pop(index)
                    logger.info(f"Task marked as done and removed: {removed_task}")
                    print("Task marked as done.")
                else:
                    logger.warning(f"Invalid task number entered: {usr_input}")
                    print("Invalid task number.")
            except ValueError:
                logger.warning(f"Non-integer input for task number: {usr_input}")
                print("Please enter a valid number.")
            print("-" * 50)

        elif x == "4":
            logger.info("User exited the to-do list.")
            print("Exiting.")
            print("-" * 50)
            break

        else:
            logger.warning(f"Invalid menu choice entered: {x}")
            print("Invalid choice.")
            print("-" * 50)

# Run the to-do list
to_do_list()