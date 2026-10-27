#!/usr/bin/python3
import sys


if len(sys.argv) > 1 :
    print("none")
else:
    i = 0;
    j = 0;
    while i < 11:
        print ("Table de" , i , end=": " )
        while j < 11:
            print(i*j, end=" ")
            j += 1    
        print()
        j = 0
        i += 1 













# for count in range(0, 11):
#     print ("Table de" , count , end=": " )
#     for line in range(0, 11):
#         print(line*count, end=" ")
#     print()
