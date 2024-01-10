print("Welcome to Prictor")
print("Choose a Category")
print("1-Automobile 2-Laptop 3-Phone 4-Tv 5-Washing Machine")
i=int(input("Please enter number associated with selected category:"))
if i==5:
    a=int(input("Input initial price of Washing Machine in Indian Rupees:"))
    b=int(input("Input how old is the Washing Machine in years:"))
    c=int(input("Input Condition of the Washing Machine on a scale of 1-5:"))
    h = a;
    if b>=1 or b<2:
        h=h*0.925
    elif b>=2 or b<3:
        h=h*0.875
    elif b>=3 or b<4:
        h=h*0.825
    elif b>=4 or b<5:
        h=h*0.800
    else:
        h=h*0.775
    if c==5:
        h=h*0.95
    elif c==4:
        h=h*0.90
    elif c==3:
        h=h*0.825
    else:
        h=h*0.775
    print("The current value of washing machine is:",h)
elif i==1:
    a=int(input("Input initial price of Automobile in Indian Rupees:"))
    b=int(input("Input how old is the Automobile in years:"))
    c=int(input("Input Condition of the Automobile on a scale of 1-5:"))
    d=int(input("Input how much the Automobile has been driven in km:"))
    h = a;
    if b>=1 or b<2:
        h=h*0.925
    elif b>=2 or b<3:
        h=h*0.875
    elif b>=3 or b<4:
        h=h*0.825
    elif b>=4 or b<5:
        h=h*0.800
    else:
        h=h*0.775
    if c==5:
        h=h*0.95
    elif c==4:
        h=h*0.90
    elif c==3:
        h=h*0.825
    else:
        h=h*0.775
    if d<10000:
        h=h*0.87
    elif d>=10000 or d<25000:
        h=h*0.84
    elif d>=25000 or d<50000:
        h=h*0.800
    elif d>=50000 or d<90000:
        h=h*0.775
    else:
        h=h*0.700
    print("The current value of the Automobile is:",h)

elif i==2:
    a=int(input("Input initial price of Laptop in Indian Rupees:"))
    b=int(input("Input how old is the Laptop in years:"))
    c=int(input("Input Condition of the Laptop on a scale of 1-5:"))
    e=input("Are there any upgrades done to the Laptop(yes/no):")
    f=input("Is the charger included(yes/no):")
    h = a;
    if b>=1 or b<2:
        h=h*0.925
    elif b>=2 or b<3:
        h=h*0.875
    elif b>=3 or b<4:
        h=h*0.825
    elif b>=4 or b<5:
        h=h*0.800
    else:
        h=h*0.775
    if c==5:
        h=h*0.95
    elif c==4:
        h=h*0.90
    elif c==3:
        h=h*0.825
    else:
        h=h*0.775
    if e=="yes" or e=="YES" or e=="Yes":
        h=h*1.05
    else:
        h=h
    if f=="yes" or f=="YES" or f=="Yes":
        h=h
    else:
        h=h*0.925
    print("The current value of the Laptop is",h)
    
elif i==3:
    a=int(input("Input initial price of Phone in Indian Rupees:"))
    b=int(input("Input how old is the Phone in years:"))
    c=int(input("Input Condition of the Phone on a scale of 1-5:"))
    e=input("Are there any upgrades done to the Phone(yes/no):")
    f=input("Is the charger included(yes/no):")
    h = a;
    if b>=1 or b<2:
        h=h*0.925
    elif b>=2 or b<3:
        h=h*0.875
    elif b>=3 or b<4:
        h=h*0.825
    elif b>=4 or b<5:
        h=h*0.800
    else:
        h=h*0.775
    if c==5:
        h=h*0.95
    elif c==4:
        h=h*0.90
    elif c==3:
        h=h*0.825
    else:
        h=h*0.775
    if e=="yes" or e=="YES" or e=="Yes":
        h=h*1.05
    else:
        h=h
    if f=="yes" or f=="YES" or f=="Yes":
        h=h
    else:
        h=h*0.925
    print("The current value of the mobile phone is:",h)
elif i==4:
    a=int(input("Input initial price of the TV in Indian Rupees:"))
    b=int(input("Input how old is the TV in years:"))
    c=int(input("Input Condition of the TV on a scale of 1-5:"))
    f=input("Is the charger included(yes/no):")
    g=input("Is the remote included(yes/no):")
    h = a;
    if b>=1 or b<2:
        h=h*0.925
    elif b>=2 or b<3:
        h=h*0.875
    elif b>=3 or b<4:
        h=h*0.825
    elif b>=4 or b<5:
        h=h*0.800
    else:
        h=h*0.775
    if c==5:
        h=h*0.95
    elif c==4:
        h=h*0.90
    elif c==3:
        h=h*0.825
    else:
        h=h*0.775
    if f=="yes" or f=="YES" or f=="Yes":
        h=h
    else:
        h=h*0.925
    if g=="yes" or g=="YES" or g=="Yes":
        h=h
    else:
        h=h*0.925
    print("The current value of the TV:",h)
else:
        print("Please select a valid option")

