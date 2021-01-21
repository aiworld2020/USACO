"""
ID: aryanra2
LANG: PYTHON3
TASK: palsquare
"""

b = 0


def getB():
    f = open("palsquare.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    b = splitted[0]
    return int(b)


def getSquare(n):
    return n * n


def getNumberForBase(num, base):
    new_num = 0
    str_num = str(num)[::-1]
    #print(str_num)
    for i in range(len(str_num)):
        new_num += int(str_num[i]) * pow(base, i)
    return new_num


def checkPalindrome(num):
    str_num = str(num)
    reverse_num = str_num[::-1]
    return str_num == reverse_num

def to_base(num, base):
    num_list = []
    dummy = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    num_str = ""
    while num:
        s = num % base
        num = int(num / base)
        
        if s >= 10:
            diff = s - 10
            num_list.append(dummy[diff])
        else:
            num_list.append(str(s))
    
    for i in range(len(num_list)):
        num_str = num_str + num_list[i]
    num_str = num_str[::-1]
    return num_str
#print(to_base(227, 11))
# print(getNumberForBase(227, 11))
#print(getNumberForBase(107009, 11))
# print(to_base(73441, 11))
print(to_base(73441, 11))



def main():
    output_list = []
    b = getB()
    max_num = 300
    for num in range(1, max_num + 1):
        square = getSquare(num)
        #n = getNumberForBase(square, b)
        
        if checkPalindrome(to_base(square, b)):
            output_list.append((to_base(num, b), to_base(square, b)))
    return output_list

def outputFile():
    with open("palsquare.out", mode = "w") as f:
        for i in range(len(output_list)):
            f.write(str(output_list[i][0]) + " " + str(output_list[i][1]) + "\n")

            
output_list = main()
outputFile()
#print(getNumberForBase(11, 2))
#print(getNumberForBase(1001, 2))
