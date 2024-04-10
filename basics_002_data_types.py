# Python Basics: Data Types

# English Video: https://www.youtube.com/watch?v=OpaV15_FW6s
# Tamil Video: https://www.youtube.com/watch?v=T8A5xSJt7FM

# Data Types in Python
# Type 1: Numeric (Integers , Floats and Complex Numbers)
#####
# Integers (whole numbers => positive or negative)
i = 12
type(i) # shows the data type

# perform operation in integer
print(-10+100, type(-10 + 100))

#####
# Float
12 + 0.25
type(12 + 0.25)

#####
# complex
12 + 3j
type(12 + 3j)

# If I have an imaginary number, then how to get the real and imaginary numbers separatly?
a = 12 + 3j
a.real
a.imag

##################################################################################
# Boolean

# it has only two builtin types
True / False

type(True)
type(False)

# this is used mainly for comparison operators
type(1 > 10)
type(1 == 1)

# Also, its Case sensitive and can't use quotes around the value
type('True')
type(TRUE)     # NameError


##################################################################################
# Strings (Immutable)

a = 'Hello World!'
b = "Hello World!"
c = """Twinkle Twinkle Little Star
Rajini is our
Super Star"""

# difference between calling the variable directly and through print() function
c
print(c)

#####
# How to represent a string with single quotes?
# a = 'I've always wanted to eat ice cream'
a = "I'have always wanted to eat ice cream"
a = """I'have always wanted to eat ice cream"""

# string can be indexed
a = 'Hello World!'
a[:5]

# a[::]
# first parameter is the starting index position
# second parameter is the end index position.
# third paramter shows how many index to skip

a[0:5]
a[0:5:2]
a[::-1]


##################################################################################
# List
[] - solid brackets for -> list
() - curve brackets for -> tuple
{} - curly brackets for -> set and dictionary


# List (Mutable)
# list can store multiple separate values
lst = [1,2,3]

# you can have any data type in a list
lst = ['Meta',2004]

# its ordered data type, that means, we can extract the element from exact position
lst = ['Cookie Dough','Strawberry','Apple']
lst[0]

# list within list
lst2 = ['Cookie',['Dough','biscuite'],'Apple']
lst2
lst2[1]
lst2[1][0]

# list is mutable
lst2 = ['Cookie',['Dough','biscuite'],'Apple']
lst2[-1] = 'Orange'
lst2

# you can append the list
lst2.append('Apple')
lst2

# you can insert in a particular position
lst2.insert(0,'Pineapple')
lst2

##################################################################################
# tuples (Imputable)
# its used when data is not going to change tha often, like country name

t = (1,2,3,1)
type(t)
t[1]
t.append(3) # AttributeError

##################################################################################
# Sets (Immutable and Unordered data type)

s = {1,2,3}
type(s)
s[1]        # TypeError

# you can add elements to set
s.add(4)
s

# it accepts adding duplicate values but stores only distinct elements
s.add(1)
s

# operations we can do in set
s1 = {1,2,3,4,5}
s2 = {0,1,1,1,2,3,4,4,4}

# s1 = {1,2,3,4,5}
# s2 = {0,1,2,3,4}

s1 | s2 # OR
s1 & s2 # AND
s1 - s2 # remove s2 from s1
s2 - s1 # remove s1 from s2
s1 ^ s2 # either in s1 or s2 but not in both. its like XOR exclusive OR


##################################################################################
# dictionary (combination of key, value pair and mutable)

d = {'Company':'Meta', 'Started':2004, 'Sub':['Facebook','Whatsapp','Instagram','Reality Labs']}
# d[0] can't use index , but can use keys
d['Company']

# update a key value
d['Sub'][1]
d['Sub'].append('FB Payments')
d

# to get only the keys
d.keys()
# to get only the values
d.values()
# to get both key and values
d.items()
