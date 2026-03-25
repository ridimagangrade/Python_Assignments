import shapes

def main():
    print("--- Geometry Calculator ---")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    try:
        choice = int(input("Enter your choice (1-3): "))
        
        if choice == 1:
            r = float(input("Enter radius: "))
            area = shapes.area_circle(r)
            print(f"Area of Circle: {area:.2f}")

        elif choice == 2:
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            area = shapes.area_rectangle(l, w)
            print(f"Area of Rectangle: {area:.2f}")

        elif choice == 3:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = shapes.area_triangle(b, h)
            print(f"Area of Triangle: {area:.2f}")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

# This ensures the script only runs if executed directly
if __name__ == "__main__":
    main()