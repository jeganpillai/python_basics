# Python Operators 
#### 1. Arithmetic Operators (7)
#### 2. Comparison Operators (6)
#### 3. Logical Operators (3)

# Arithmeric Operators
"""
+ : Addition 
- : Subtraction 
* : Multiplication 
/ : Division 

// : Integer Division 
%  : Modulus Operator 
** : Exponent 
"""

# Addition 
a = 1 
b = 5
print(a + b)

# Subtraction 
a = 5 
b = 1
print(a - b)

# Multiplication 
a = 5 
b = 4
print(a * b)

# Division 
a = 50 
b = 4
print(a / b)

# Integer Division 
a = 50 
b = 4
print(a // b)

# Modulus 
a = 50 
b = 4
print(a % b)

# Exponent 
a = 10 
b = 4
print(a ** b)

# Arithmetic Operators with different data types 
a = 10 
b = 4
c = 'Grow With Data'
# print(a/b, ' and type is: ', type(a//b))
print(c * b)

a = 'Grow With '
b = 'Data'
print(a + b)

################################################
# Comparison Operators
"""
== : Equal To 
!= : Not Equal To
>  : Greater Than
<  : Less Than 
>= : Greater Than or Equal To
<= : Less Than or Equal To
"""

# Equal To 
a = 10 
b = 20 
print(a == b) # 10 == 20? 

# Not Equal To 
a = 10 
b = 20 
print(a != b) # 10 != 20? 

# Greater Than
a = 10 
b = 20 
print(a > b) # 10 > 20? 

# Less Than
a = 10 
b = 20 
print(a < b) # 10 < 20? 

# Greater Than OR Equal To 
a = 10 
b = 20
print(a >= b) # 10 >= 20? 

# Less Than OR Equal To 
a = 10 
b = 20
print(a <= b) # 10 <= 20? 

################################################
# Logical Operators 
"""
AND 
OR 
NOT 
"""

# AND 
a = 10 
b = 20
c = 30 

print(a > b and a > c) # False and False 

# True AND True => True 
# True AND False => False 
# False AND True => False 
# False AND False => False 

# OR 
a = 25 
b = 20
c = 30 

print(a > b or a > c) # True OR False 

# True OR True => True 
# True OR False => True 
# False OR True => True 
# False OR False => False 

# NOT 
a = 25 
b = 20
c = 30 

print(not(a > b ))

# True => False 
# False => True 
