def main():
    while True:
        print("\n=== Automation Hub ===")
        print("1. Say Hello")
        print("2. Show Version")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            print("Hello, McswazStingHub-Ltd!")

        elif choice == "2":
            print("Automation Hub v2.0")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
