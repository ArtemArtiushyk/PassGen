import random
import string


def generate():
    try:
        length = int(input("Length of your new password: "))
        characters = string.ascii_letters + string.digits
        password = ""

        for i in range(length):
            password += random.choice(characters)
        print(
            f"""
            Your new generated password:
            {password}
            """
        )
    except ValueError:
        print(
            """
            >>>> Length shouldn't contain any other symbols except numbers.
            >>>> Length must be a whole number.
            >>>> Length shouldn't be empty.
            """
        )
    except KeyboardInterrupt:
        print("\n\n>>>> You quitted. Goodbye!\n")


generate()
