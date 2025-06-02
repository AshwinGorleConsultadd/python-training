list1 = input("Enter first list elements separated by space: ").split()
list2 = input("Enter second list elements separated by space: ").split()

set1 = set(list1)
set2 = set(list2)

common_elements = set1.intersection(set2)

print("Common elements:", list(common_elements))
