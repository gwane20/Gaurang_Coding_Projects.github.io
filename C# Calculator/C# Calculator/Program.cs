
class Calculator
{
    static void Main(string[] args)
    {
        Console.WriteLine("  Calculator  ");

        bool continueCalc = true;

        while (continueCalc)
        {
            try
            {
                // Operation menu
                Console.WriteLine("\nChoose an operation:");
                Console.WriteLine("1. Addition (+)");
                Console.WriteLine("2. Subtraction (-)");
                Console.WriteLine("3. Multiplication (*)");
                Console.WriteLine("4. Division (/)");
                Console.WriteLine("5. Exit");

                //User input for the operation they need to perform.
                Console.Write("\nEnter your choice (1-5): ");
                int choice = int.Parse(Console.ReadLine()); 

                if (choice == 5)
                {
                    Console.WriteLine("Calculator Closed.");
                    continueCalc = false;
                    break;
                }

                // Getting user input for calculation
                Console.Write("Enter the first number: ");
                double num1 = double.Parse(Console.ReadLine());

                Console.Write("Enter the second number: ");
                double num2 = double.Parse(Console.ReadLine());

                double result = 0;

                // Perform the chosen operation
                switch (choice)
                {
                    case 1:
                        result = num1 + num2;
                        Console.WriteLine($"Result: {num1} + {num2} = {result}");
                        break;

                    case 2:
                        result = num1 - num2;
                        Console.WriteLine($"Result: {num1} - {num2} = {result}");
                        break;

                    case 3:
                        result = num1 * num2;
                        Console.WriteLine($"Result: {num1} * {num2} = {result}");
                        break;

                    case 4:
                        if (num2 == 0)
                        {
                            Console.WriteLine("Error: Division by zero is not possible.");
                        }
                        else
                        {
                            result = num1 / num2;
                            Console.WriteLine($"Result: {num1} / {num2} = {result}");
                        }
                        break;

                    default:
                        Console.WriteLine("Invalid choice. Please select a valid operation.");
                        break;
                }
            }
            catch (FormatException)
            {
                Console.WriteLine("Invalid input. Please enter a valid number.");
            }
        }
    }
}
