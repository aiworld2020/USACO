"""
ID: aryanra2
LANG: PYTHON3
TASK: transform
"""
import numpy as np

def getBefore(n, splitted):
    before = ""
    before_list = []
    print("n = ", n)
    for i in range(1, n + 1):
        before = splitted[i]
        before = before.replace("@", '2 ')
        before = before.replace("-", '1 ')
        before = before.split(" ")
        del before[-1]
        before_list.append(before)
    
    print("inside getbefore = ", before_list)
    return before_list

def getAfter(n, splitted):
    after = []
    after_list = []
    for i in range(n + 1, n * 2 + 1):
        after = splitted[i]
        after = after.replace("@", '2 ')
        after = after.replace("-", '1 ')
        after = after.split(" ")
        del after[-1]
        after_list.append(after)
    return after_list


def checkRot(before_list, after_list):
    print(before_list)
    print(after_list)
    before_list = np.array([np.array(xi) for xi in before_list])
    after_list = np.array([np.array(xi) for xi in after_list])
    comparison1 = np.rot90(before_list) == after_list
    comparison2 = np.rot90(before_list, 2) == after_list
    comparison3 = np.rot90(before_list, 3) == after_list
    if comparison1.all():
        return 3
    
    elif comparison2.all():
        return 2
    
    elif comparison3.all():
        return 1
    else:
        return -1



def checkFlip(before_list, after_list):
    before_list = np.array([np.array(xi) for xi in before_list])
    after_list = np.array([np.array(xi) for xi in after_list])
    comparison1 = np.fliplr(before_list) == after_list
    comparison2 = np.rot90(np.fliplr(before_list)) == after_list
    comparison3 = np.rot90(np.fliplr(before_list), 2) == after_list
    comparison4 = np.rot90(np.fliplr(before_list), 3) == after_list
    if comparison1.all():
        return 4
    
    elif comparison2.all() or comparison3.all() or comparison4.all():
        return 5
    else:
        return -1

def checkOther(before_list, after_list):
    
    before_list = np.array([np.array(xi) for xi in before_list])
    after_list = np.array([np.array(xi) for xi in after_list])
    comparison = before_list == after_list
    if comparison.all():
        return 6
    elif checkRot(before_list, after_list) == -1 and checkFlip(before_list, after_list) == -1:
        return 7
    
    else:
        return -1


def main():
    f = open("transform.in", mode = 'r')
    content = f.read()
    splitted = content.split("\n")
    
    n = int(splitted[0])

    before_list = getBefore(n, splitted)
    after_list = getAfter(n, splitted)
    
    print(before_list)
    print(after_list)
    print("**")
    check1 = checkRot(before_list, after_list)
    
    print("check1 = ", check1)
    check2 = checkFlip(before_list, after_list)
    check3 = checkOther(before_list, after_list)
    
    if check1 != -1:
        return check1
    
    else: 
        check2 = checkFlip(before_list, after_list)
        
        if (check2 != -1):
            return check2
        
        else:
            check3 = checkOther(before_list, after_list)
            return check3

def outputFile():
    with open("transform.out", mode = "w") as f:
        f.write(str(trans) + "\n")
        
trans = main()
outputFile()
    
