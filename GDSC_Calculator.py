import math

def calculator():
    while True:
        try:
            expression = input("Enter a mathematical expression (or 'quit' to exit): ")
            
            if expression.lower() == 'quit':
                break
            
            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    calculator()
