import random
import string
from tkinter import *


class Tkinter:
    def generate_tk():
        def menu():
            @staticmethod
            def generate():
                try:
                    length = int(tent1.get())
                    characters = string.ascii_letters + string.digits
                    password = ""

                    for i in range(length):
                        password += random.choice(characters)

                    ttex1.delete("1.0", END)
                    ttex1.insert(END, password)

                except ValueError:
                    tlab4[
                        "text"
                    ] = """
            >>>> Length shouldn't contain any other symbols except numbers.
        >>>> Length must be a whole number.
    >>>> Length shouldn't be empty.
                """

            top = Toplevel(root)
            top.geometry("500x600+650+82")
            top.title("Generator menu")

            tlab1 = Label(top, text="Amount of symbols.", font="Arial 18")
            tlab1.pack()

            tent1 = Entry(top, width=20)
            tent1.pack()

            tbut1 = Button(top, text="Generate", command=generate)
            tbut1.pack()

            ttex1 = Text(top, height=20, width=50)
            ttex1.pack()

            tlab2 = Label(
                top,
                text="""^
The password will come here.""",
                font="Arial 18",
            )
            tlab2.pack()

            tlab3 = Label(
                top,
                text="""^
You can scroll btw""",
                font="Arial 18",
            )
            tlab3.pack()

            tlab4 = Label(top, text="", font="Arial 11")
            tlab4.pack()

        root = Tk()
        root.geometry("600x600")
        root.title("Welcome")

        lab1 = Label(root, text="PassGen", font="Arial 60")
        lab1.pack()

        lab2 = Label(
            root,
            text="Generate password with as many symbols as you want.",
            font="Arial 18",
        )
        lab2.pack()

        but1 = Button(root, text="Generate password", command=menu)
        but1.pack()

        root.mainloop()


class Cli:
    def generate_cli():
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


try:
    ask = input("CLI or TK(c/T): ").upper()
    if ask == "C":
        Cli.generate_cli()
    elif ask == "T":
        Tkinter.generate_tk()
    else:
        Tkinter.generate_tk()
except KeyboardInterrupt:
    print("\n\n>>>> You quitted. Goodbye!\n")
