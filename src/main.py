import os


def show_system_info():
    print("\n=== System Information ===")
    print(f"Current directory: {os.getcwd()}")
    print(f"Operating System: {os.name}")


def notes_manager():
    note = input("Enter a note: ")

    with open("notes.txt", "a") as f:
        f.write(note + "\n")

    print("Note saved.")


def view_notes():
    try:
        with open("notes.txt", "r") as f:
            print("\n=== Saved Notes ===")
            print(f.read())
    except FileNotFoundError:
        print("No notes found.")


def main():
    while True:
        print("\n=== Automation Hub ===")
        print("1. Say Hello")
        print("2. Show Version")
        print("3. System Information")
        print("4. Add Note")
        print("5. View Notes")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("Hello, McswazStingHub-Ltd!")

        elif choice == "2":
            print("Automation Hub v4.0")

        elif choice == "3":
            show_system_info()

        elif choice == "4":
            notes_manager()

        elif choice == "5":
            view_notes()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
