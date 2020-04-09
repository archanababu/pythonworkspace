#-------------------------------
# Reading a file
# open function is used to open the file
#  - Parameters passed inside the open functions are, path and the mode of the file
#  - path of the file can be :
#            - relative path of the file
#            - absolute path of the file
#            - just the file name, if its in the same directory
#  - mode of the file can be :
#            - r -> read mode
#            - w -> write mode
#            - a -> append mode. Append information at the end of the file
#            - r+ -> both read and write mode
#------------------------------

employeefile = open("employees.txt","r")
#print(employeefile.read())
#print(employeefile.readline())
#print(employeefile.readlines())
for employee in employeefile.readlines():
    print(employee)
employeefile.close()

#---------------------------------
# Writing and Appending in a file
#---------------------------------

#Append - Adds to the end of the file

employeefile = open("employees.txt","a")
employeefile.write("\nGlenda - Manager")
employeefile.close()

#Write - Overwrites the file

employeefile = open("employees.txt","w")
employeefile.write("Gavin - Business owner")
employeefile.close()

#Creating a new file using the write mode

employeefile = open("index.html","w")
employeefile.write("<p> HTML page </p>")
employeefile.close()



