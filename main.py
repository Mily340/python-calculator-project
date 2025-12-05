class Calculator:
    """
    A fully functional calculator class with arithmetic operations,
    input validation, and menu-driven interface.
    """
    
    def __init__(self):
        """Initialize the calculator."""
        self.operations = {
            '1': ('Add', self.add),
            '2': ('Subtract', self.subtract),
            '3': ('Multiply', self.multiply),
            '4': ('Divide', self.divide)
        }
    
    # Step 1: Create Arithmetic Functions
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide two numbers with division-by-zero safety."""
        if b == 0:
            return "Error: Division by zero is not allowed!"
        return a / b
    
    # Step 3: Input Validation
    def get_valid_number(self, prompt):
        """
        Get a valid number from user input with error handling.
        
        Args:
            prompt (str): The message to display to the user
            
        Returns:
            float: A valid number entered by the user
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    # Step 5A: Menu Method
    def menu(self):
        """Display the calculator menu options."""
        print("\n" + "="*40)
        print("           CALCULATOR MENU")
        print("="*40)
        for key, (name, _) in self.operations.items():
            print(f"{key}. {name}")
        print("5. Exit")
        print("="*40)
    
    # Step 5B: Run Method
    def run(self):
        """
        Main method to run the calculator program.
        Displays menu, takes user input, and performs operations.
        """
        print("Welcome to the Python Calculator!")
        
        while True:
            self.menu()
            choice = input("Please select an operation (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break
            
            if choice in self.operations:
                # Get two numbers from the user
                print(f"\n{self.operations[choice][0]} Operation:")
                num1 = self.get_valid_number("Enter the first number: ")
                num2 = self.get_valid_number("Enter the second number: ")
                
                # Perform the selected operation
                operation_name, operation_func = self.operations[choice]
                result = operation_func(num1, num2)
                
                # Display the result in formatted way
                if isinstance(result, str):  # Error message for division by zero
                    print(f"Result: {result}")
                else:
                    # Format the operation symbol
                    if choice == '1':
                        symbol = '+'
                    elif choice == '2':
                        symbol = '-'
                    elif choice == '3':
                        symbol = '*'
                    elif choice == '4':
                        symbol = '/'
                    
                    print(f"Result: {num1} {symbol} {num2} = {result}")
            else:
                print("Invalid choice! Please select a valid option (1-5).")

# Step 2 & 4: Standalone functions for earlier steps demonstration
def demonstrate_arithmetic_functions():
    """Demonstrate the arithmetic functions with user input."""
    calc = Calculator()
    
    print("Step 2: Arithmetic Functions Demonstration")
    print("Enter two numbers to see all operations:")
    
    num1 = calc.get_valid_number("First number: ")
    num2 = calc.get_valid_number("Second number: ")
    
    # Perform and display all operations
    print(f"\nOperations with {num1} and {num2}:")
    print(f"Addition: {num1} + {num2} = {calc.add(num1, num2)}")
    print(f"Subtraction: {num1} - {num2} = {calc.subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {calc.multiply(num1, num2)}")
    
    division_result = calc.divide(num1, num2)
    if isinstance(division_result, str):
        print(f"Division: {division_result}")
    else:
        print(f"Division: {num1} / {num2} = {division_result}")

def menu_driven_calculator():
    """Demonstrate a simple menu-driven calculator (Step 4)."""
    calc = Calculator()
    
    print("\nStep 4: Menu-Driven Calculator")
    print("This demonstrates the calculator without OOP structure")
    
    while True:
        print("\nSimple Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Select operation (1-5): ").strip()
        
        if choice == '5':
            print("Returning to main calculator...")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = calc.add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == '2':
                    result = calc.subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == '3':
                    result = calc.multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == '4':
                    result = calc.divide(num1, num2)
                    if isinstance(result, str):
                        print(result)
                    else:
                        print(f"{num1} / {num2} = {result}")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please select 1-5.")

# Step 5C: Create Calculator object and run the program
if __name__ == "__main__":
    # Demonstrate all steps
    print("PYTHON CALCULATOR PROJECT")
    print("="*50)
    
    # Uncomment the following lines to see step-by-step demonstration
    # demonstrate_arithmetic_functions()
    # menu_driven_calculator()
    
    # Final OOP Calculator
    print("\nFinal Object-Oriented Calculator:")
    calculator = Calculator()
    calculator.run()