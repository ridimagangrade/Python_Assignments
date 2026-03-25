def convert(celsius):
    return celsius + 273.15

value = float(input("Enter Celsius: "))
print(f"Result: {convert(value)} K")