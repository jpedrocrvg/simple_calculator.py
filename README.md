# Calculator Python Script
This simple Python script is a basic calculator that performs four arithmetic operations: addition, multiplication, subtraction, and division. Users can input two numbers and choose an operation to perform on those numbers.

## Usage

1) Run the script in a Python environment.

2) Enter the first number when prompted.

3) Enter the second number when prompted.

4) Choose an operation from the available options (+, *, -, /).

The script will then display the result of the chosen operation on the two input numbers.

## Code Explanation
The script defines four functions for basic arithmetic operations:

add(n1, n2): Returns the sum of two numbers.
multiply(n1, n2): Returns the product of two numbers.
subtract(n1, n2): Returns the result of subtracting the second number from the first.
divide(n1, n2): Returns the result of dividing the first number by the second.
These functions are stored in a dictionary named operations, where each operation is associated with its corresponding function.

The script then prompts the user to input two numbers. Afterward, it displays the available operations and asks the user to choose one. The selected operation is used to retrieve the corresponding function from the operations dictionary.

Finally, the script executes the chosen function on the input numbers and displays the result.
