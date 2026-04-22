#Opeming and writing
file = open("sample.txt", "w")
file.write("This is getting appended. \n")
file.close()


file = open("sample.txt", "r")
print("The opening is done")
content = file.read()
print("The contents are \n", content)
file.close()

file = open("sample.txt", "a")
file.write("This is an appended line")
file.close()

file = open("sample.txt", "r")
content_final = file.read()
print(f"The final content is:\n{content_final}")
