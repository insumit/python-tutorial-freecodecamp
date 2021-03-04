# Basic input output from users
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + " years old!")

# Reading files
# Read r, Write w, Append a, Read and Write r+
employee_file = open("employees.txt", "r")
print(employee_file.readable())
print(employee_file.read())
# Reads the next line
# readlines() reads the lines and store in a list
# print(employee_file.readlines()[1])

for employee in employee_file.readlines():
    print(employee)

print(employee_file.readline())

employee_file.close()
employee_file = open("employees.txt", "a")

employee_file.write("Toby - Human Resources")
employee_file.write("\nKelly - Customer Service")

employee_file.close()

# Over-writes
employee_file = open("employees.txt", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

# New file
employee_file = open("employees-new.txt", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()
