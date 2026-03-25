def convert(fahrenheit):
    return (fahrenheit - 32) * 5/9

value = float(input("Enter Fahrenheit: "))
print(f"Result: {convert(value)}°C")