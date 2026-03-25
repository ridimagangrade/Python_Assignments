#Creating a Set
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
print("Original set1:", set1)
print("Original set2:", set2)

#Add Element
set1.add(60)
print("After adding(60):", set1)

#Remove Element
set1.remove(20)
print("After the removal(20):", set1)

#Set Union
print("Union:", set1.union(set2))

#Set Intersection
print("Intersection:", set1.intersection(set2))

#Set Difference
print("Difference:", set1.difference(set2))

#Symmetric Difference 
print("Symmetric Difference:", set1.symmetric_difference(set2))