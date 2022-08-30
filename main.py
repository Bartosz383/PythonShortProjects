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
    print("A. Addition \nB. Substaction \nC. Multiplication \nD. Division \nE. Exit")

    choice = input("Input your choice: ")

    a = int(input("Input first number: "))
    b = int(input("Input second number: "))

    opr = Operations()

    if choice =="a" or choice == "A":
        print("Addition" + str(opr.add()))
    elif choice == "b" or choice == "B":
        print("Substration" + opr.sub())
    elif choice == "c" or choice == "C":
        print("Multiplication" + opr.mul())
    elif choice == "d" or choice == "D":
        print("Division" +  opr.div())
    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()
    else:
        print("Invalid choice")

