'''
TITLE   :WAP FOR PYTHON CONDITIONAL AND ITERATIVE STATEMENTS
NAME    :RAHUL S. VISHWAKARMA
ROLL NO.:1076
'''

# IF STATEMENTS

print("IF STATEMENTS:-")
a=50
b=25
if(a>b):
    print("a is greater than b ")
    
# IF..ELSE STATEMENTS

print("IF..ELSE STATEMENTS:-")
a=25
b=50
if(a>b):
    print("a is greater than b ")
else:
    print("a is less than b ")

# IF..ELIF STATEMENTS

print("IF..ELIF STATEMENTS:-")
a=25
b=25
if(a>b):
    print("a is greater than b ")
elif(a==b):
    print("both are equal ")

# IF..ELIF..ELSE STATEMENTS

print("IF..ELIF..ELSE STATEMENTS:-")
a=100
b=25
if(a>b):
    print("b is greater than a ")
elif(a==b):
    print("both are equal ")
else:
    print("a is greater than b ")

# NESTED IF

print("NESTED IF:-")
a=31
if(a>10):
    print("a is greater than 10")
    if(a>20):
        print("a is greater than 20")
        if(a>30):
            print("a is greater than 30")
            if(a>40):
                print("a is greater than 40")
                if(a>50):
                    print("a is greater than 50")
                else:
                    print("a is between 40 to 50")
            else:
                print("a is between 30 to 40")
        else:
            print("a is between 20 to 30")
    else:
        print("a is between 10 to 20")
else:
    print("a is between 0 to 10")

# WHILE LOOP

print("WHILE LOOP:-")
i=1
while(i<6):
    print(i)
    i+=1

# NESTED WHILE LOOP

print("NESTED WHILE LOOP:-")
i=1
j=5
while(i<5):
    while(j<9):
        print(i," ",j)
        j+=1
        i+=1

# THE BREAK WHILE STATEMENTS

print("THE BREAK WHILE STATEMENTS:-")
i=1
while(i<6):
    print(i)
    if(i==4):
        break
    i+=1

# THE CONTINUE WHILE STATEMENTS

print("THE CONTINUE WHILE STATEMENTS:-")
i=-1
while(i<5):
    while(i<9):
        i+=1
        if(i==5):
            continue
        print(i)



    
















    
