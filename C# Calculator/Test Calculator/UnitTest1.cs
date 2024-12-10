using NUnit.Framework; // Required for NUnit test framework

namespace CalculatorTests
{
    [TestFixture] // Marks this class as a test fixture
    public class CalculatorTests
    {
        private Calculator calculator;

        [SetUp] // Runs before each test
        public void Setup()
        {
            calculator = new Calculator(); // Initialize calculator instance
        }

        [Test] // Marks this method as a test case
        public void TestAddition_ValidInputs_ReturnsCorrectResult()
        {
            double result = calculator.Add(5, 3);
            Assert.AreEqual(8, result, "Addition result is incorrect.");
        }

        [Test]
        public void TestSubtraction_ValidInputs_ReturnsCorrectResult()
        {
            double result = calculator.Subtract(10, 4);
            Assert.AreEqual(6, result, "Subtraction result is incorrect.");
        }

        [Test]
        public void TestMultiplication_ValidInputs_ReturnsCorrectResult()
        {
            double result = calculator.Multiply(6, 7);
            Assert.AreEqual(42, result, "Multiplication result is incorrect.");
        }

        [Test]
        public void TestDivision_ValidInputs_ReturnsCorrectResult()
        {
            double result = calculator.Divide(15, 3);
            Assert.AreEqual(5, result, "Division result is incorrect.");
        }

        [Test]
        public void TestDivision_DivisionByZero_ThrowsException()
        {
            Assert.Throws<System.DivideByZeroException>(() => calculator.Divide(10, 0), "Division by zero should throw exception.");
        }
    }

    // Calculator class
    public class Calculator
    {
        public double Add(double num1, double num2) => num1 + num2;
        public double Subtract(double num1, double num2) => num1 - num2;
        public double Multiply(double num1, double num2) => num1 * num2;

        public double Divide(double num1, double num2)
        {
            if (num2 == 0)
                throw new System.DivideByZeroException("Cannot divide by zero.");
            return num1 / num2;
        }
    }
}
