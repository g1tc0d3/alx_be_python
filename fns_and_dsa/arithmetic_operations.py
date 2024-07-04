def perform_operation(num1, num2, operation):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = str(input("Enter the operation (add, subtract, multiply, divide): "))

    match operation:
        case "add":
            print (num1 + num2)
        case "subtract":
            print (num1 - num2)
        case "multiply":
            print (num1 * num2)
        case "divide":
            if num2 == 0:
                print ("Cannot recognize and display correctly")
            else:
                print (num1 / num2)
perform_operation()
