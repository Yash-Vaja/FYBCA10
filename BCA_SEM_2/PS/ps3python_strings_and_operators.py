'''
TITLE   :WAP FOR PYTHON STRINGS ANSD OPERATORS
NAME    :RAHUL S. VISHWAKARMA
ROLL NO.:1076
'''

# SINGLE LINE STRINGS

print("SINGLE LINE STRINGS:-")
a ="Hello!"
print(a)

# MULTI LINE STRINGS

print("MULTI LINE STRINGS:-")
a ="""
My name is Rahul
I am studying in BCA
"""
b="""
Sutex bank college of
computer applications
and science
"""
print(a)
print(b)

# STRING ARE CHARACTER ARRAYS

print("STRING ARE CHARACTER ARRAYS:-")
a="Hello,World!"
print(a[0])
print(a[1])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(a[10])

# LOOPING THROUGH A STRING

print("LOOPING THROUGH A STRING:-")
for x in "Rahul":
    print(x)

# SLICING STRINGS

print("SLICING STRINGS:-")
b="Hello,World!"
print(b[2:5])

# SLICE FROM THE START

print("SLICE FROM THE START:-")
b="Hello,World!"
print(b[:5])

# SLICE TO THE END

print("SLICE TO THE END:-")
b="Hello,World!"
print(b[2:])

# NEGATIVE INDEXING

print("NEGATIVE INDEXING:-")
b="Hello,World!"
print(b[-5:-2])


# STRING METHODS #

# CENTER

print("CENTER:-")
txt="Rahul"
x=txt.center(50)
print(x)

#COUNT

print("COUNT:-")
txt="Sutex Bank College,R.V. Patel College "
x=txt.count("College")
print(x)

# JOIN

print("JOIN:-")
txt=("I","am","Rahul")
x=" ".join(txt)
print(x)

# LEN

print("LEN:-")
r="Hello,World!"
x=len(r)
print(x)

# MAX

print("MAX:-")
txt="ABCD"
x=max(txt)
print(x)

# MIN

print("MIN:-")
txt="ABCD"
x=min(txt)
print(x)

# REPLACE

print("REPLACE:-")
txt="my my name is rahul , college is sutex"
x=txt.replace("my","i")
print(x)

# LOWER

print("LOWER:-")
txt="Hello my World"
x=txt.lower()
print(x)

# UPPER

print("UPPER:-")
txt="Hello my World"
x=txt.upper()
print(x)

# SPLIT

print("SPLIT:-")
txt="Welcome in my World"
x=txt.split()
print(x)

# IDENTITY OPERATOR

print("IDENTITY OPERATOR:-")
x=5
y=10
print(x is y)
print(x is not y)

# MEMBER OPERATOR

print("MEMBER OPERATOR:-")
x=("mango","apple")
print("mango" in x)

y=("mango","apple")
print("mango" not in y)















