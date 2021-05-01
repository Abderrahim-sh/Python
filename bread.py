#!/usr/bin/python3
import os
import sys
if os.path.isfile(str(sys.argv[1])):
    f=open(sys.argv[1],"rb")
    for i in f.readlines():
        print(i)
else:
    print("bread: cannot access {}: No such file ".format(sys.argv[1]))
