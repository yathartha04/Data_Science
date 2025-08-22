#August 20
#Task :Create a fully functional calculator system using loop

# while True:
#         choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for exit: "))
#         if choice == 5:
#             print("Exiting")
#             break
#         n1 = int(input("Enter a number: "))
#         n2 = int(input("Enter another number: "))
#         match choice:
#             case 1:
#                 print("The sum is: ", n1+n2)
#             case 2:
# 	            print("The difference is: ", n1-n2)
#             case 3:
#                 print("The multiplication is: ", n1*n2)
#             case 4:
# 	            print("The division is: ", n1/n2)
#             case _:
#                 print("invalid input")

#August 21
#Task 1. Write a function to do division and multiplication

# choice = int(input("1 for multiplication, 2 for division: "))
# def multiply():
#     n1 = int(input("Enter a number: "))
#     n2 = int(input("Enter another number: "))
#     print(n1*n2)

# def divide():
#     n1 = int(input("Enter a number: "))
#     n2 = int(input("Enter another number: "))
#     print(n1/n2)
# match choice:
#     case 1:
#         multiply()
#     case 2:
#         divide()
#     case _:
#         print("Invalid instruction")

#Task 2. Update the calculator using function and using keyword or positional arguments and use loop

# while True:
#     choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for division, 4 for multiplication, 5 for power, 6 for modulus, 7 for floor division, 8 for exit: "))
#     if choice == 8:
#      print("Exiting")
#      break
#     if range(1,8):
#      num1 = int(input("Enter first number: "))
#      num2 = int(input("Enter second number: "))   
#     def addition(num1, num2):  
#         print(f"{num1+num2}")
#     def subtraction(num1, num2):
#         print(f"{num1-num2}")
#     def division(num1, num2):
#         print(f"{num1/num2}")
#     def multiplication(num1, num2):
#         print(f"{num1*num2}")
#     def power():
#         print(f"{num1**num2}")
#     def modulus():
#         print(f"{num1%num2}")
#     def floor_division(num1, num2):
#         print(f"{num1//num2}")
#     match choice:
#         case 1:
#             addition(num1, num2)
#         case 2:  
#             subtraction(num1, num2)
#         case 3:
#             division(num1, num2)
#         case 4:  
#             multiplication(num1, num2)
#         case 5:
#             power()
#         case 6:  
#             modulus()
#         case 7:
#             floor_division(num1, num2)    
#         case _:
#             print("Invalid Operation")

#August 22
#Task 1.Use list comprehension to find even numbers from 1 to 100 (100 is inclusive)

list1 = list(range(1, 101))
list2 = [x for x in range(1,101) if x % 2 == 0] 
print(list2)
