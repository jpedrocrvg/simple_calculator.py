def add(n1, n2):
  return n1 + n2

def multiply(n1, n2):
  return n1 * n2

def subtract(n1,n2):
  return n1 - n2

def divide(n1,n2):
  return n1/n2

operations = {}

operations["+"] = add
operations["*"] = multiply
operations["-"] = subtract
operations["/"] = divide

def calculate():
  should_continue = True
  num1 = int(input('What is the first number? '))
  while should_continue:
    
    num2 = int(input('What is the second number? '))
    operation_sign = input('What is the operation that you want to do?') 
    calculation_function = operations[operation_sign]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_sign} {num2} = {answer}")
  
    if input(f"Do you want to continue working with {answer}? Y or N ").upper() == 'Y':
      num1 = answer
    else:
      should_continue = False
      calculate()
