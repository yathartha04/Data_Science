#August 19
#Task 1.Create a list of usernames and take a username from the user, check if the username is present in the list or not.

# username = ["yathartha29","simba619","james","silva","terry"]
# a = input("Enter your username: ")
# if a in username:
#     print("Username already exists")
# else:
#     print("New username created")

#Task 2.Create a simple calculator system.

# choice = input("Enter + for addition ,- for subtraction ,* for multiplication , / for division: ")
# n1 = int(input("Enter a number: " ))
# n2 = int(input("Enter another number: "))
# match choice:
#     case '+':
#         print("The sum is: ", n1+n2)
#     case '-':
#         print("The difference is: ", n1-n2)
#     case '*':
#         print("The multiplication is: ", n1*n2)
#     case '/':
#         print("The division is: ", n1/n2)
#     case _:
#         print("invalid input")

#Task 3.Create a simple calculator system.

# n1 = int(input("Enter a number: " ))
# n2 = int(input("Enter another number: "))
# operation = input("Enter the operation: ")
# if operation == '+':
#     print(n1+n2)
# elif operation == '-':
#     print(n1-n2)
# elif operation == '*':
#     print(n1*n2)
# elif operation == '/':
#     print(n1/n2)
# elif operation == '**':
#     print(n1**n2)
# elif operation == '%':
#     print(n1%n2)
# elif operation == '<':
#     print(n1<n2)
# elif operation == '>':
#     print(n1>n2)
# elif operation == '//':
#     print(n1//n2)
# else :
#     print("Invalid operation")

#Task 4.Create a dictionary of usernames and passwords,extract all the usernames from the dictionary and input username from the user and check if the username is present in the extracted list of usernames.

# lab = {"yathartha":"yat123","lampard":"8","terry":"3","drogba":"11"}


#Task 5.Make a complete register and login system using dictationary.

task = {

}
username = input("Enter your username: ")
password = input("Enter your password: ")

task.update()
print(task)

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in task and task.get(username) == password: # credentials[username] == password:
    print("Login Successful")
else:
    print("Login failed")


#Task 6.Find the greatest number among three number, number is given by user.

# j = int(input("Enter first number: "))
# p = int(input("Enter second number: "))
# g = int(input("Enter third number: "))
# if j > p and j > g:
#     print("Greatest number: ",j)
# elif p > j and p > g:
#     print("Greatest number: ",p)
# elif g > j and g > p:
#     print("Greatest number: ",g)
# else :
#     print("System Error")