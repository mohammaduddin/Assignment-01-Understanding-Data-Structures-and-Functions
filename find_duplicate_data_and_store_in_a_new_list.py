# Problem: 03
# Write a Python program that creates a new list containing only the duplicate
# elements from the given list: [1, 5, 6, 5, 1, 2, 3].

data_list = [1, 5, 6, 5, 1, 2, 3]

# initialize an empty set to store seen elements
unique_data_set = set()

# list to store duplicates
new_list = []

for n in data_list:
    if n in unique_data_set:
        new_list.append(n)
    else:
        unique_data_set.add(n)

print(new_list)


# OUTPUT:
# [5, 1]