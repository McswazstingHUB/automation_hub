import secrets
import string


def generate_password():
    try:
        length = int(input("Password length (8-64): "))

        if length < 8 or length > 64:
            print("Length must be between 8 and 64.")
            return

        chars = (
            string.ascii_letters
            + string.digits
            + "!@#$%^&*()_+-="
        )

        password = ''.join(
            secrets.choice(chars)
            for _ in range(length)
        )

        print("\n=== Generated Password ===")
        print(password)

    except ValueError:
        print("Please enter a valid number.")
