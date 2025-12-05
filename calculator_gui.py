import tkinter as tk
from tkinter import ttk, messagebox
from main import Calculator

class CalculatorGUI:
    """
    A graphical user interface for the Calculator using tkinter.
    """
    
    def __init__(self, root):
        """Initialize the GUI calculator."""
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("450x550")
        self.root.resizable(False, False)
        
        # Initialize the calculator backend
        self.calculator = Calculator()
        
        # Calculator state
        self.current_number = ""
        self.previous_number = None
        self.operation = None
        self.display_var = tk.StringVar(value="0")
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create and layout all GUI widgets."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Display screen - using tk.Entry instead of ttk.Entry for better display
        display_frame = ttk.Frame(main_frame)
        display_frame.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=10)
        display_frame.columnconfigure(0, weight=1)
        
        # Use regular tk.Entry for better display support with proper width
        display = tk.Entry(display_frame, textvariable=self.display_var, 
                           font=("Arial", 24, "bold"), state="readonly", 
                           justify="right", relief="flat", bd=5, bg="#f0f0f0",
                           width=20)
        display.grid(row=0, column=0, sticky=(tk.W, tk.E), ipady=10, padx=5)
        
        # Button style - use regular tk.Button instead of ttk.Button for font support
        button_style = {"font": ("Arial", 14), "width": 8, "height": 2}
        
        # Number buttons (7-9) - using tk.Button instead of ttk.Button
        tk.Button(main_frame, text="7", command=lambda: self.number_click("7"), **button_style).grid(row=1, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="8", command=lambda: self.number_click("8"), **button_style).grid(row=1, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="9", command=lambda: self.number_click("9"), **button_style).grid(row=1, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="÷", command=lambda: self.operation_click("divide"), **button_style).grid(row=1, column=3, padx=2, pady=2)
        
        # Number buttons (4-6)
        tk.Button(main_frame, text="4", command=lambda: self.number_click("4"), **button_style).grid(row=2, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="5", command=lambda: self.number_click("5"), **button_style).grid(row=2, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="6", command=lambda: self.number_click("6"), **button_style).grid(row=2, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="×", command=lambda: self.operation_click("multiply"), **button_style).grid(row=2, column=3, padx=2, pady=2)
        
        # Number buttons (1-3)
        tk.Button(main_frame, text="1", command=lambda: self.number_click("1"), **button_style).grid(row=3, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="2", command=lambda: self.number_click("2"), **button_style).grid(row=3, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="3", command=lambda: self.number_click("3"), **button_style).grid(row=3, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="−", command=lambda: self.operation_click("subtract"), **button_style).grid(row=3, column=3, padx=2, pady=2)
        
        # Number button 0, Clear, Equals, Add
        tk.Button(main_frame, text="0", command=lambda: self.number_click("0"), **button_style).grid(row=4, column=0, padx=2, pady=2)
        tk.Button(main_frame, text="C", command=self.clear_click, **button_style).grid(row=4, column=1, padx=2, pady=2)
        tk.Button(main_frame, text="=", command=self.equals_click, **button_style).grid(row=4, column=2, padx=2, pady=2)
        tk.Button(main_frame, text="+", command=lambda: self.operation_click("add"), **button_style).grid(row=4, column=3, padx=2, pady=2)
        
        # Decimal point button
        tk.Button(main_frame, text=".", command=lambda: self.number_click("."), **button_style).grid(row=5, column=0, padx=2, pady=2, columnspan=4, sticky=(tk.W, tk.E))
    
    def number_click(self, digit):
        """Handle number button clicks."""
        if digit == "." and "." in self.current_number:
            return  # Don't allow multiple decimal points
        
        # If current_number is empty or "0", replace it (unless it's a decimal point)
        if self.current_number == "" or self.current_number == "0":
            if digit == ".":
                self.current_number = "0."
            else:
                self.current_number = digit
        else:
            self.current_number += digit
        
        self.display_var.set(self.current_number)
    
    def operation_click(self, op):
        """Handle operation button clicks."""
        if self.current_number:
            if self.previous_number is not None and self.operation:
                # Calculate previous operation first
                self.calculate()
            
            self.previous_number = float(self.current_number)
            self.operation = op
            self.current_number = ""
            self.display_var.set("0")
    
    def equals_click(self):
        """Handle equals button click."""
        if self.previous_number is not None and self.operation and self.current_number:
            self.calculate()
    
    def calculate(self):
        """Perform the calculation using the Calculator class."""
        if self.previous_number is None or not self.operation or not self.current_number:
            return
        
        try:
            num1 = self.previous_number
            num2 = float(self.current_number)
            
            # Use the Calculator class methods
            if self.operation == "add":
                result = self.calculator.add(num1, num2)
            elif self.operation == "subtract":
                result = self.calculator.subtract(num1, num2)
            elif self.operation == "multiply":
                result = self.calculator.multiply(num1, num2)
            elif self.operation == "divide":
                result = self.calculator.divide(num1, num2)
            else:
                return
            
            # Handle error messages
            if isinstance(result, str):
                messagebox.showerror("Error", result)
                self.clear_click()
            else:
                # Format result (remove unnecessary decimals)
                if result == int(result):
                    result_str = str(int(result))
                else:
                    # Remove trailing zeros
                    result_str = f"{result:.10f}".rstrip('0').rstrip('.')
                
                # Update display
                self.display_var.set(result_str)
                self.current_number = result_str
                self.previous_number = None
                self.operation = None
                
        except ValueError:
            messagebox.showerror("Error", "Invalid number!")
            self.clear_click()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.clear_click()
    
    def clear_click(self):
        """Handle clear button click."""
        self.current_number = ""
        self.previous_number = None
        self.operation = None
        self.display_var.set("0")

def main():
    """Run the GUI calculator."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()