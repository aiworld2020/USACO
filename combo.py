"""
ID: aryanra2
LANG: PYTHON3
TASK: combo
"""

def getNumber(n, max_n):
    possible = [n]
    if(n+1 <= max_n):
        possible.append(n+1)
    else:
        possible.append(abs(n + 1 - max_n))
    
    if(n+2 <= max_n):
        possible.append(n+2)
    else:
        possible.append(abs(n+2 - max_n))
    
    if(n-2 > 0):
        possible.append(n-2)
    else:
        possible.append(abs(n-2 + max_n))
    
    if(n-1 > 0):
        possible.append(n-1)
    else:
        possible.append(abs(n-1 + max_n))
        
    print(possible)
    return possible


def main():
    answer1 = []
    answer2 = []
    combo = 0
    f = open("combo.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    
    max_n = int(splitted[0])
    list1 = splitted[1].split(" ")
    list2 = splitted[2].split(" ")
    
    list1 = [int(x) for x in list1]
    list2 = [int(x) for x in list2]
    
    for i in list1:
        answer1.append(getNumber(i, max_n))
        
    
    for i in list2:
        answer2.append(getNumber(i, max_n))
    for i in range(1, max_n + 1):
        for j in range(1, max_n + 1):
            for k in range(1, max_n + 1):
                if (i in answer1[0] and j in answer1[1] and k in answer1[2]) \
                    or (i in answer2[0] and j in answer2[1] and k in answer2[2]):
                        combo += 1
    return combo

def outputFile(combo):
    f = open("combo.out", mode = "w")
    f.write(str(combo) + "\n")

if __name__ == "__main__":
    combo = main()
    outputFile(combo)