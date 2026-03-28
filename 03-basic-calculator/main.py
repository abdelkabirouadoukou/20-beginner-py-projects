# define the functions needed: add, sub, mul, div
# print options to the user
# ask for values
# call the funs
# while loop to continue the progran until the user wants to exit

def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

def sub(a,b):
    answer = a-b
    print(f"{a} - {b} = {answer}")

def mul(a,b):
    answer = a*b
    print(f"{a} * {b} = {answer}")

def div(a,b):
    answer = a/b
    print(f"{a} / {b} = {answer}")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input ur choice: ")
    if choice == "a" or choice == "A":
        print("Addition")
        a = float(input("input first number:"))
        b = float(input("input second number:"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = float(input("input first number:"))
        b = float(input("input second number:"))
        sub(a,b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = float(input("input first number:"))
        b = float(input("input second number:"))
        mul(a,b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = float(input("input first number:"))
        b = float(input("input second number:"))
        div(a,b)
    elif choice == "e" or choice == "E":
        print("program ended")
        exit()
    else:
        print("Command not found")