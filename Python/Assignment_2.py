#Task aug 14: input for every data type we discussed and print it

#num = int(input("Enter a whole number: "))
#print(num)

#float1 = float(input("Enter a number: "))
#print(float1)

#name = input("Enter your email address: ")
#print(name)

#Task aug 15: ask two numbers from the user
#Perform operation on those numbers or values


# a = int(input("Enter one number: "))
# b = int(input("Enter another number: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a//b)
# print(a%b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a==b)
# print(a!=b)


#Task: Ask user a string and print, if 'b' is in that string or not

# a = input("Write a word: ")
# if "b" in a:
#     print("b is present")
# else:
#     print("b is absent")


#Task aug 17: Implement all the indexing and slicing in string also

g = [1,2,3,4,5,"yathartha",[9,8,7,6],"game"]

#1.append()-adds element at the end of the list
g.append("plan")
print(g)

#2.count()-
print(g.count(4))

#3.extend()-
name = ["bamba","hood","thought"]
g.extend(name)
print(g)

#4.insert()-
g.insert(0,["zero"])
print(g)

#5.pop()-
g.pop(0)
print(g)

#6.remove()-
g.remove("yathartha")
print(g)

#7.reverse()-
g.reverse()
print(g)

#8.sort()-

#9.index()-
print(g.index("game"))

#Slicing-Create a new subset list from the original list
# b = a[0:5] # - The end value is always exclusive( The end value is not sliced)

w = [1,3,5,7,9,"hola",["boom",619],"espanyol"]

#10.Start to end slicing
f = w[4:6]
print(f)

#11.End slicing
f = w[:7]
print(f)

#12.Start slicing
f = w[4:]
print(f)

#13.Positive index with step
f = w[::2]
print(f)

#14.Negative Index
print(w[-5])

#15.Slicing in Negative indexing
print(w[-5:-1:])

# We also have same indexing and slicing in Python strings
# Task : Implement all the indexing and slicing in string also

name = "demigod"

#indexing
print(name[0]) #+ve indexing
print(name[-1]) #-ve indexing
print(name[-5:-1]) #negative slicing
print(name[0:5]) #+ve slicing
print(name[0:7]) #start-end slicing
print(name[:7]) #end slicing
print(name[0:]) #start slicing
print(name[::2]) #+ve index with step
#-ve index with step

#Task 18 aug: 
#Tuple-Tuple is a immutable data type in python that wraps the element in ().
c = (1,3,5,7,9,11,2,3,5,3,6,3,8,9,2,3)
print(c.count(3))

print(c.index(11))
