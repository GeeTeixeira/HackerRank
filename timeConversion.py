#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = s[0:2]
    last = s[len(s)-2:len(s)]
    if hour == "12" and last == "AM":
        return "00"+s[2:-2]
    if last == "PM" and hour == "12":
        return s[0:-2]
    if last == "PM":
        hour = str(int(hour) + 12)
        if int(hour) <24:
            return hour+s[2:-2]
        if int(hour) == 24:
            return "00"+s[2:-2]
    if last == "AM" and int(hour) <12:
        return s[0:-2]
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
