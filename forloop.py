#----------------------
# For loop
#----------------------

for letter in "Learning Python":
    print(letter)

for index in range(5):
    print(index)

for index in range(3,5):
    print(index)

friends = ["Anna","Jim","Troy","Alex"]

for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])


#-----------------------------
# 2D List and Nested loop
#-----------------------------

numberGrid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in numberGrid:
    for col in row:
        print(col)
