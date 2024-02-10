from calculator import Calculator
calculator1=Calculator()
def main():
    # created instance of the calculator class
    
    stay=True
    while(stay):
        display()
        option=input()
        match option:
            case "1":
                add()
            case "2":
                subract()
            case "3":
                multiply()
            case "4":
                division()
            case "5":
                help()
            case "6":
                stay=False
            





def add():
    num1,div,num2=input("Enter a number you want to add in this format (num1 + num2): ").split()
    print(calculator1.add(int(num1),int(num2)))
def subract():
    num1,div,num2=input("Enter a number you want to subtract in this format (num1 - num2): ").split()
    print(calculator1.subtract(int(num1),int(num2)))
def multiply():
    num1,div,num2=input("Enter a number you want to multiply in this format (num1 * num2): ").split()
    print(calculator1.multiply(int(num1),int(num2)))
def division():
    num1,div,num2=input("Enter a number you want to divide in this format (num1 / num2): ").split()
    print(calculator1.divide(int(num1),int(num2)))

def help():
    print("---Instruction about the calculator---")
    print("Choose option 1 to add, make sure you follow the format (num1 + num2)!")
    print("Choose option 2 to subtract, make sure to follow the format (num1 - num2)! ")
    print("Choose option 3 to multiply, make sure to follo the format (num1 * num2)! ")
    print("Choose option 4 to divide, make sure to follow the format (num1 / num2 ), num2 != 0.")
    print("Choose option 5 for help")
    print("Choose option 6 to exit.")

def display():
    print("---Welcome to simple calculator---")
    print("1. add")
    print("2, subtract")
    print("3, multiply")
    print("4, divide")
    print("5, Help")
    print("6, exit.")
    print("Enter your option: ")
    
main()