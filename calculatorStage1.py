#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("float division by zero")
        return None
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    return a % b

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    if choice == '+':
        return add
    elif choice == '-':
        return subtract
    elif choice == '*':
        return multiply
    elif choice == '/':
        return divide
    elif choice == '^':
        return power
    elif choice == '%':
        return remainder
    elif choice == '#':
        return -1
    elif choice == '$':
        return 'reset'
    else:
        print("Unrecognized operation")
        return -1



#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()
    
  # Reset condition
  if choice == '$':
    continue

  # Validate if the choice is a valid operation
  if select_op(choice) != -1:
    try:
        # Get operands for arithmetic operations
        num1 = input("Enter first number: ").strip()
        print(num1)
        if num1 == '$':
            continue
        if num1 == '#':
            print("Done. Terminating")
            exit()
        
        # Check if '$' is present in the operand, in which case reset
        if '$' in num1:
            continue  # Return to the main menu if '$' is detected
        # Check if '#' is present in the operand, in which case terminate
        if '#' in num1:
            print("Done. Terminating")
            exit()  # Return to the main menu if '#' is detected
            
        num2 = input("Enter second number: ").strip()
        print(num2)
        if num2 == '$':
            continue
        if num2 == '#':
            print("Done. Terminating")
            exit()
        
        # Check if '$' is present in the operand, in which case reset
        if '$' in num2:
            continue  # Return to the main menu if '$' is detected
        if '#' in num2:
            print("Done. Terminating")
            exit()  # Return to the main menu if '#' is detected

        # Convert inputs to float
        num1 = float(num1)
        num2 = float(num2)
            
        # Perform the operation
        operation = select_op(choice)
        result = operation(num1, num2)

        # If division by zero occurs or operation is invalid, handle it
        if result is None:
            print(f"{num1} {choice} {num2} = None")
        else:
            print(f"{num1} {choice} {num2} = {result}")

    except ValueError:
        print("Not a valid number, please enter again")
    except Exception:
        print("Something Went Wrong")
  else:
    continue