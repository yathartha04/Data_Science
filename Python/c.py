#1. Create a program to take a string input from the user and print its length.

# enter = input("Enter a string: ")
# calcu = len(enter)  #len() calculates the number of characters in that string (including spaces and punctuation).
# print(calcu)

# 2. Write a program to convert a list of strings into a list of integers.

# string = [1,2,3,4,5]
# integer = [int(i) for i in string]
# print(integer)

# 3. Write a program to check if a given number is even or odd.

# num = int(input("Enter a number: "))    
# if num % 2 == 0 :
#     print("It is an even number.")
# else:
#     print("It is an odd number")
    

# 4. Write a program to find the largest of three numbers entered by the user.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a > b and a > c:
#     print(f"{a} is the greatest number.")
# elif b > a and b > c:
#     print(f"{b} is grestest number.")
# elif c > a and c > b:
#     print(f"{c} is the greatest number.")
# else:
#     print("Tie among numbers")

# 5. Write a program to print the multiplication table of a given number.2

# num = int(input("Enter a number to get multiplication table: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# 6. Write a program to print all numbers from 1 to 50 that are divisible by 5.

# num = [x for x in range(1,51) if x % 5 == 0] 
# print(num)

# 7. Write a program to count how many vowels are present in a given string.

# enter = input("Enter a string: ")
# vowels = "aeiouAEIOU" 
# count = 0
# for char in enter:
#  if char in vowels:
#   count += 1
#   print(count)

# 8. Write a program to print the factorial of a number using a while loop.

num = int(input("Enter a number: "))
factorial = 1
i = 1
i <= num:
    
    factorial += 1
    print(factorial)



# 9. Write a function to check whether a given number is prime or not.

# while :
#     num = int(input("Enter a number: "))
#     if num % 2 == 0 :
   

# 10. Write a function to reverse a string without using built-in functions like [::-1] or reversed().
# def rev_str():
#     string1 = "GAME"
#     rev_string = ""
#     for char in string1:
#      rev_string = char + rev_string
#      print(rev_string)  
