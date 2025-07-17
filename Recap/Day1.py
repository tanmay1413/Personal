#  Comments in python 
# # it used for single line comment 


# Multi-line comment 
'''
asdjflsjafasfldjl
jshflafjosajlfs
nlsalkfjsalk
nsdjflkasjfl
'''

# Print 

print("Hello world ...")
print(123)

# Escape sequance 

# sep=' '
print('09','12','2016', sep='-----')

# end 

# Variabls
# varabel is a container 
name = "Amol"  
print("type of name:",type(name))

# declaration of variabel 
# variabel are always start with  letters  
# variabel are dose not start with number and special char
#
one_1 = 123
print(type(one_1))

# Data types 
# 1) Number --> int , float , complex 
# 2) str 
# 3) boolen --> True , false

# List 
# Set
# Tupel 
# Dectonary

num = 10.5
comp = complex(12, 4)
print(type(comp)) 

# typecasting

a = "2"
b = int(a)
print(b)

c = float(b)
print(c , type(c))

#  Global variabel
#  It assign outside the function and u access that in file from anywhere
name = "Amol"
print(name)


# function define 
def student(name):
  # Local variabel 
  full_name = name
  print("This print inside the function : ",full_name)


a = student("Amol Ganesh")


# Operators 
# 1) Arthematic 
# Addition (+)
a = 2 
b = 5
c = a + b
print("Sum = ",c)

# Subtraction (-)
d = b-a
print("Subtraction = ", d)

# Division (/)
e = b / a
print("Division = ", e)

# Multiplication (*)
f = a * b
print("multiplication = ", f)

# Modulus (%)
g = b % a
print("Modulus = ",g)

"""
# check given number is even or odd 
num1 = int(input("Enter first number :"))

if num1 <= 0:
  print("Enter Positive number")
elif num1 % 2 == 0:
  print("Even")
else:
  print("Odd")

"""
# Floor division (//)
f = b // a
print("Floor division = ", f)

# Exponent (**)
g = 5 ** 2
print("Exponent = ", g)


## ---Assignment operator----
# 1) equal (=)
name = "Ajay"

# ( += )
x = 10
x += 1
print(x)

# ( -= )
x = 10
x -= 1
print(x)

# ( *= )
x = 10
x *= 10
print(x)

# ( /= )
x = 10
x /= 10
print(x)

# ( //= )
x = 10
x //= 7
print(x)

# ( %= )
x = 10
x %= 7
print(x)

# ( **= )
x = 10
x **= 10
print(x)

# logical operator 
# 1) and  ---> both conditions are true 
# 2) or   ---> At least one condition is True
# 3) not  ---> Reverse condtion 

a , b = 10 , 21
if a == 10 or b == 20 :
  print("done")
else:
  print("Faild")


# Membership operator 
# 1) in
# 2) not in

li = [10, 20 ,30]
if 30 not in li:
  print("True")
else:
  print("False")


# Identity operator 
#  1) is 
#  2) not is 

a = [1, 2, 3]
b = a   

if a is not b:
    print("a is b")     
else:
    print("a is not b")



# Condition statements 
# if , elif , else

# Q1) check the marks of the student and give the result 
#  condition > 35 pass
# < 35 fail
# > 80 first class 
"""
number = int(input("enter the mark :"))

if number < 0 :
   print("enter Correct marks!!!!")
elif number > 80:
    print("First class")
elif number > 35 and number < 80:
    print("Pass")
else:
    print("fail")
"""

# Q2) If height is grater than 160 cm and age is grater than 18 print selected other wise not selected 

"""
height =  int(input("Enter height :"))
age =  int(input("Enter age :"))

if age >= 18 and height >= 160:
   print("Selected ....")
else:
   print("Not Selected...")

"""

# Q3) write a program to calculate the electrcity bill take input from user for number of unit used 
"""
    Unit            Price 
first 100 units      Free(Rs.0)
next 100 units      Rs. 5/unit
after 200 units     Rs. 10/unit
""" 

unit = int(input("enter the unit :"))
bill = 0
if unit >= 0 and unit <= 100 :
    bill = 0
elif unit > 100 and unit <= 200:
    bill = unit * 5
else:
    bill = unit * 10

print(f"The bill of {unit} is {bill}")