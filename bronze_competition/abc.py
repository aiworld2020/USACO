"""
ID: aryanra2
LANG: PYTHON3
TASK: abc
"""

import itertools as it
import sys

def main():
    splitted = sys.stdin.readlines()
    #splitted = ['2 2 11 4 9 7 9\n']
    abc_list = [int(x) for x in splitted[0].split(" ")]
    
    abc_list.sort(reverse = True)
    
    max_num = abc_list[0]
    
    combs = list(it.combinations(abc_list[1:], 3))
    
    for i in range(len(combs)):
        if sum(combs[i]) == max_num:
            answer = list(combs[i])
            answer.sort()
            return answer

def outputFile(answer):
    temp = ""
    for i in range(3):
        if i == 2:
            temp += str(answer[i])
        else:    
            temp += str(answer[i]) + " "
    print(temp)

if __name__ == "__main__":
    answer = main()
    outputFile(answer)