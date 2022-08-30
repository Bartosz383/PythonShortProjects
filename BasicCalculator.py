class Operations:
    def add(self):
        answer = a + b
        print(str(a) + " + " + str(b) + " = " +str(answer))

    def sub(self):
        answer = a - b
        print(str(a) + " - " + str(b) + " = " + str(answer))

    def mul(self):
        answer = a * b
        print(str(a) + " * " + str(b) + " = " + str(answer))

    def div(self):
        answer = a / b
        print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
    choice = input("Input your choice: ")

    a = int(input("Input first number: "))
    b = int(input("Input second number: "))

    opr = Operations()

    def menu():
        x=("A. Addition \nB. Substaction \nC. Multiplication \nD. Division \nE. Exit")
        print(x)
    menu()

    if choice == "e" or choice == "E":
        print("Program ended")
        quit()
    elif choice =="a" or choice == "A":
        print("Addition" + str(opr.add()) + "\n")
    elif choice == "b" or choice == "B":
        print("Substration" + opr.sub() + "\n")
    elif choice == "c" or choice == "C":
        print("Multiplication" + opr.mul() + "\n")
    elif choice == "d" or choice == "D":
        print("Division" +  opr.div() + "\n")
    else:
        print("Invalid choice")
