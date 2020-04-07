#------------------
# FUNCTIONS - Any code inside a function needs to be indented 
#------------------

def helloworld():
    print("Hello world in python")

helloworld()

# using parameter in function
def greetUser(name, age):
    print("Hello "+name+". You are "+str(age)+" years old")

greetUser("Anna", 28)

#------------------
# Return statement
#------------------

def cube(num):
    return num*num*num

print(cube(3))