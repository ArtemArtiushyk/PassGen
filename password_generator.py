import random
import string

try:

    def generate(length: int):
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

    leng = int(input("Length of your new password: "))
    generate(leng)

except ValueError:
    print(
        """
>>>> Length shouldn't contain any other symbols except numbers.
>>>> Length must be a whole number.
>>>> Length shouldn't be empty.
"""
    )

except KeyboardInterrupt:
    print(
        """

>>>> You quitted. Goodbye!
"""
    )
