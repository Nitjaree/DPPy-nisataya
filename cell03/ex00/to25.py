#!/usr/bin/python3
print("Enter a number less than 25")
less25=int(input())
if less25 > 25:
    print("Error")
else:
    for count in range(less25, 25):
        print ("Inside the loop, my variable is",count)