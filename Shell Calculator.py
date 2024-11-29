def add(x, y):
    return x+y
def sub(x, y):
    return x-y
def multi(x, y):
    return x*y
def divi(x, y):
    return x/y
print ("Select Operation:-")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
while True:
    choice = input("Enter Choice:- [1/2/3/4]:- ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number:- "))
            num2 = float(input("Enter second number:- "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divi(num1, num2))
    next_calculation = input("Let's do next calculation? [Yes/No]:- ")
    if next_calculation == "no":
          break
    else:
        print("Invalid Input")
