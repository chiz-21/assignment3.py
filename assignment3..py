# Step 1: Create an empty list
my_list= []
# Step 2: Append elements to the list
my_list= [10, 20, 30, 40]
print (my_list)
# Step 3: Insert the value 15 at the second position
my_list.insert(1, 15)
print (my_list)
# Step 4: Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print (my_list)
# Step 5: Remove the last element from the list
my_list.pop()
print (my_list)
# Step 6: Sort the list in ascending order
my_list.sort()
print (my_list)
# Step 7: Find and print the index of the value 30
index_of_30 =my_list.index(30)
print("Index of 30 is:", index_of_30)
