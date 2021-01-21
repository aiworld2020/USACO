"""
ID: aryanra2
LANG: PYTHON3
TASK: dualpal
"""

n = 0
s = 0
pal_list = []

f = open("dualpal.in", mode = "r")
content = f.read()
splitted = content.split("\n")

def getN():
    n = splitted[0].split(" ")[0]
    return int(n)

def getS():
    s = splitted[0].split(" ")[1]
    return int(s)


def to_base(num, base):
    num_list = []
    num_str = ""
    while num:
        s = num % base
        num = int(num / base)
        num_list.append(str(s))
    
    for i in range(len(num_list)):
        num_str = num_str + num_list[i]
    num_str = num_str[::-1]
    return num_str


def checkPalindrome(num):
    str_num = str(num)
    reverse_num = str_num[::-1]
    return str_num == reverse_num


def main():
    count = 0
    num_counter = 0
    n = getN()
    s = getS()
    i = s + 1
    while num_counter < n:
        for j in range(2, 11):
            #print(i, j)
            num = to_base(i, j)
            #print(num)
            if checkPalindrome(num):
                count += 1
                if count == 2:
                    pal_list.append(i)
                    num_counter += 1
                    break
        count = 0
        i += 1

def outputFile():
    with open("dualpal.out", mode = "w") as f:
        for i in range(len(pal_list)):
            f.write(str(pal_list[i]) + "\n")

              
main()
outputFile()

