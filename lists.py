#------------------------------
# Basics of working with lists
#------------------------------

fruits = ["Apple","Orange","Grape","Watermelon","Strawberry"]
# index      0       1        2        3             4
# reverse   -5      -4       -3       -2            -1
apple = ["Apple","red", 4]

print(fruits)
print(apple)

# Printing by its index value
print(fruits[1])

# Printing values from backwards. Starts from -1, -2, -3 and so on
print(fruits[-2])

# Printing values from index to all after that
print(fruits[2:])

# Printing values using the range
print(fruits[2:4])

#--------------
#List Functions
#--------------

# 1. Entend function: Basically take a list and append with another list
lucky_number = [5,8,10,4,14,6,27,17,4,65,4,2]
friends = ["Anna","Alex","Charlene","Jim","Troy","Rolf"]

#before 
print(friends)

friends.extend(lucky_number)

#after
print(friends)

# 2. append function: Add individual element on to the list
#                     Always add the element to the end of the list
friends.append("Darla")
print(friends)

# 3. insert function: Add element in the middle of the list. Adds at the index position and the other elements are pushed to right 
friends.insert(2,"Tim")
print(friends)

# 4. remove function: Remove an element from the list
friends.remove("Darla")
print(friends)

# 5. clear function: completely removes everything from the list or resets the list. Returns empty list
friends.clear()
print(friends)

# 6. pop function: removes an element off the list i.e., the last element off the list
lucky_number.pop()
print(lucky_number)

# 7. index function: returns the index value of an element in the list. 
print(lucky_number.index(14))

# 8. count function: counts how many times an element is repeated in the list
print(lucky_number.count(4))

# 9. sort function: sorts list in the ascending order
lucky_number.sort()
print(lucky_number)

# 10. reverse function: reverse the order of list
lucky_number.reverse()
print(lucky_number)

# 11. copy function: copies the elements from one list to another
lucky_number_copy = lucky_number.copy()
print(lucky_number_copy)


