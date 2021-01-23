"""
ID: aryanra2
LANG: PYTHON3
TASK: daisychains
"""

import sys

def readData():
    splitted = sys.stdin.readlines()
    #splitted = ['4\n', '1 1 2 3\n']
    n= int(splitted[0])
    petals = [int(x) for x in splitted[1].split(" ")]
    return n, petals

def check(t_list):
    for i in range(1, len(t_list)):
        if t_list[i] == t_list[i-1] + 1:
            continue
        else:
            return False
    return True

def solve(n, petals):
    count = 0
    while len(petals) > 0:
        for k in range(1, len(petals)+1):
            t = petals[:k]
            #print(t)
            average = sum(t)/len(t) 
            if(average in t):
                #print("pass")
                count +=1
        del petals[0]
    
    return count
      
    
if __name__ == "__main__":
    n, petals = readData()
    answer = solve(n, petals)
    print(answer)
    
    
    
    
    


