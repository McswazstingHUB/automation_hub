import os

from config import APP_NAME, VERSION, AUTHOR
from password_generator import generate_password
from network_info import show_network_info
from file_organizer import organize_downloads
from system_tools import show_system_info


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
        print(f"\n=== {APP_NAME} v{VERSION} ===")
        print(f"Developer: {AUTHOR}")
        print("1. Say Hello")
        print("2. Show Version")
        print("3. System Information")
        print("4. Add Note")
        print("5. View Notes")
        print("6. Generate Password")
        print("7. Network Information")
        print("8. File Organizer")
        print("9. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print(f"Hello, {AUTHOR}!")

        elif choice == "2":
            print(f"{APP_NAME} v{VERSION}")

        elif choice == "3":
            show_system_info()

        elif choice == "4":
            notes_manager()

        elif choice == "5":
            view_notes()

        elif choice == "6":
            generate_password()

        elif choice == "7":
            show_network_info()

        elif choice == "8":
            organize_downloads()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
