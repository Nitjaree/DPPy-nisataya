#!/usr/bin/python3
import sys
import re


if len(sys.argv)<=2:
    print("none")
else :
    result = len(re.findall(sys.argv[1],sys.argv[2]))

    print(result)

