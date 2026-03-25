# Dictionaries
# 4.1 Create and access dictionary elements
student = {
    "name": "ABC",
    "age": 19,
    "course": "BTech"
}

print("Dictionary:", student)

print("\nAccessing elements:")
print("Name:", student["name"])
print("Age:", student["age"])

# 4.2 Update Dictionary
student["age"] = 20          # change value
student["city"] = "XYZ"     # add new key

print("\nAfter updating dictionary:")
print(student)

# 4.3 Removing Elements
student.pop("course")        # remove one item

print("\nAfter removing an element:")
print(student)

# 4.4 Merging Dictionaries
extra = {
    "year": 2026,
    "college": "ABC College"
}

student.update(extra)

print("\nAfter merging dictionaries:")
print(student)