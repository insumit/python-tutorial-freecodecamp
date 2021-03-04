# Classes and Objects
from Student import Student

student1 = Student("Jim", "Business", 3.2, False)
student2 = Student("Pam", "Physics", 2.2, True)

print(student1.gpa)
print(student2.name)

print(student1.on_honor_roll())