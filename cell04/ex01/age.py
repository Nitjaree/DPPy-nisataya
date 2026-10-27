#!/usr/bin/python3
age = int(input("Please tell me your age: "))
print("You are currently", str(age) ,"years old.")
for i in range (1,4):
    print("In", str(i*10) , "years, you'll be", str(age+i*10) , "years old.")
# In 10 years, you'll be 25 years old.
# In 20 years, you'll be 35 years old.
# In 30 years, you'll be 45 years old.