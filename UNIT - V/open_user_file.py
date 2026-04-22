'''
Create a program that takes a filename from the user and tries to open the file for reading and handle these exceptions and provide appropriate error messages for following cases.
1.1) FileNotFoundError: If the file does not exist.
2.2) PermissionError: If the program lacks permissions to read the file.
'''

import collections

def process_file_with_structures():
    # 1. Get filename from user
    filename = input("Enter the name of the file to read: ")

    # Initialize Stack (List) and Queue (Deque)
    stack = []
    queue = collections.deque()

    try:
        # 2. Try to open and read the file
        with open(filename, 'r') as file:
            print(f"\n--- Successfully opened '{filename}' ---")
            
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    stack.append(clean_line)  # Push to Stack
                    queue.append(clean_line)  # Enqueue

        # Demonstrate data structure output
        print("\n[Data in Stack (Top first)]:")
        while stack:
            print(f"Popped: {stack.pop()}")

        print("\n[Data in Queue (Front first)]:")
        while queue:
            print(f"Dequeued: {queue.popleft()}")

    # 3. Handle FileNotFoundError
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the path.")

    # 4. Handle PermissionError
    except PermissionError:
        print(f"Error: You do not have the required permissions to read '{filename}'.")

    # Handle any other unexpected errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    process_file_with_structures()






























'''
try:
    with open ("./file.txt", 'r') as file:
    
        content = file.read()
        print(content)

        file.seek(0)

        readlines = file.readlines()
        print(readlines)

        print(file.tell())

except FileNotFoundError as error:
    print(f"{error} occured!")

except PermissionError as error:
    print(f"{error} occured!")
'''
