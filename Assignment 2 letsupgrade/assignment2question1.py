#Write a Python program to remove empty List from List-
#Program
list1 = [5, 6, [], 3, [], [], 9]
print("The original list is : " + str(list1))
list2 = [ele for ele in list1 if ele != []]
print("List after empty list removal : " + str(list2))