#!/usr/bin/python3
import sys
import os

for i in range(len(sys.argv)):
    if i == 0:
        print(os.path.basename(sys.argv[0]))
    else:
        print(sys.argv[i])
