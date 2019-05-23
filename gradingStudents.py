#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    i = 0
    import math
    while i <len(grades):
        temp = grades[i]%10
        if temp>=8 and grades[i] >=38:
            grades[i] = int(math.ceil(grades[i] / 10.0)) * 10
        if grades[i]>40 and (temp>=3 and temp<=5):
            grades[i] = grades[i]-temp+5
        i+=1
    return grades
            

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
