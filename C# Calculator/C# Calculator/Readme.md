# Console-Based Calculator in C#

This is a simple console-based calculator application written in C#. The calculator performs basic arithmetic operations such as addition, subtraction, multiplication, and division. It also includes input validation and error handling to ensure a smooth user experience.

## Features:

- Perform basic arithmetic operations
    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
- Prevents division by zero with error handling.
- Handles invalid inputs gracefully using a try-catch block.
- Allows the user to perform multiple calculations in one session.
- Option to exit the calculator at any time.

## Sample Output

  Calculator

Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

Enter your choice (1-5): 1
Enter the first number: 12
Enter the second number: 8
Result: 12 + 8 = 20

Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

Enter your choice (1-5): 4
Enter the first number: 10
Enter the second number: 0
Error: Division by zero is not allowed.

Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

Enter your choice (1-5): 5

Calculator Closed.


## Code Overview
The code uses a while loop to keep the calculator running until the user chooses to exit. Here's an overview of the key sections:

1. Menu Display: The program displays a menu of operations.
2. User Input: Users input their choice of operation and two numbers.
3. Error Handling: The program handles invalid inputs and prevents division by zero.
4. Switch-Case Logic: Operations are performed based on the user's choice.
5. Exit Option: Users can exit the program at any time by selecting option 5.
