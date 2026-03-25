#Creating a List
my_list=[10,20,30,40,50]
print("Original List:" , my_list)

#Indexing
print("Element at Index 2:" ,my_list[2])

#Slicing 
print("List from Index 1 to 3:" ,my_list[1:4])

#Append 
my_list.append(60)
print("After Append(60):" ,my_list)

#Insert (Add element at specific index)
my_list.insert(2,25)
print("After insert(2,25):" ,my_list)

#Remove 
my_list.remove(40)
print("After Removing(40):" ,my_list)

#Update Element
my_list[0]=5
print("After updating index from 0 to 5:" ,my_list)

#Reversing
my_list.reverse()
print("After Reversing:" ,my_list)