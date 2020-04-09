#-------------------------------------------------------------
# Classes and Objects
# - Create your own data type using class 
# - Define your own data type
#
#-------------------------------------------------------------

from student import Student
from chineseChef import ChineseChef
from chef import Chef

student1 = Student("1111", "Anna", "Business", 3.1, False)
student2 = Student("2222", "Alex", "Computer Science", 3.8, False)
print(student2.name)

# Using object functions
print(student2.isOnHonorRoll())

mychef = Chef()
mychineseChef = ChineseChef()

mychef.makeSpecialDish()
mychineseChef.makeSpecialDish()