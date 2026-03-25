def convert(celsius):
    return (celsius * 9/5) + 32

value = float(input("Enter Celsius: "))
print(f"Result: {convert(value)}°F")