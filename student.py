class Student:
     def __init__(self, studentID, name, major, gpa, isOnProbation):
         self.studentID = studentID
         self.name = name
         self.major = major
         self.gpa = gpa
         self.isOnProbation = isOnProbation    
     def isOnHonorRoll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False

