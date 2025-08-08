# Get first set of integers from the user
set1_input = input("Enter numbers for the first set (separated by spaces): ")
set1 = {int(num) for num in set1_input.split()}

# Get second set of integers from the user
set2_input = input("Enter numbers for the second set (separated by spaces): ")
set2 = {int(num) for num in set2_input.split()}

# Find common elements (intersection)
common_set = set1.intersection(set2)  

# Display the results
print("\nFirst set:", set1)
print("Second set:", set2)
print("Common elements:", common_set)
