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