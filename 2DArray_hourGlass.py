#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    lenArray = len(arr[0])
    arrUnit = len(arr)
    hourGlass = -1000000
    
    hourGTop = 0
    rangeTop = 3
    hourGMid = 1
    hourGBottom  = 0
    rangeBot = 3
    indexArray = 0
    while indexArray<=3:
          totalVal = sum(arr[indexArray][hourGTop:rangeTop])+arr[indexArray+1][hourGMid]+sum(arr[indexArray+2][hourGBottom:rangeBot])
          if totalVal>hourGlass:
                    hourGlass = totalVal
          hourGTop +=1
          rangeTop +=1
          hourGMid +=1
          hourGBottom +=1
          rangeBot +=1
          if hourGTop>3:
                    hourGTop = 0
                    rangeTop = 3
                    hourGMid = 1
                    hourGBottom  = 0
                    rangeBot = 3
                    indexArray+=1
          print(indexArray,totalVal)

    return hourGlass
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
