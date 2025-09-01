#Create an empty list
my_list = []
print("Before append:", my_list)

# Append elements individually
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After append:", my_list)

# Insert 15 at the second position (index 1)
my_list.insert(1,15)
print("After inserting 15 at position 2:", my_list)

# Extend with another list [50, 60, 70]
another_list = [50, 60, 70]
my_list.extend(another_list)
(print("After extending with [50, 50, 70]:", my_list)

 # Remove the last element (70)
 my_list.pop()
print("After removing the last element:", my_list)

# Sort the list in ascending order
my_list.sort()
print("After sorting in ascending:", my_list)

# Find and print index of 30
index_of_30 = my_list.index(30)
print("The index of value 30 is:", index_of_30)