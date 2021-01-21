"""
ID: aryanra2
LANG: PYTHON3
TASK: crypt1
"""
import itertools as it

def checkNum(num, num_list):
    num = str(num)
    for i in range(len(num)):
        if int(num[i]) in num_list:
            continue
        else:
            return False
    return True

def convert(num_list): 
    s = [str(i) for i in num_list] 
      
    res = int("".join(s)) 
      
    return res 


def main():
    digits3 = []
    digits2 = []
    answer = 0
    f = open("crypt1.in", mode = 'r')
    content = f.read()
    splitted = content.split("\n")
    del splitted[-1]
    n = int(splitted[0])
    num_list = splitted[1].split(" ")
    
    num_list = [int(x) for x in num_list]
    
    list_str = (''.join([str(elem) for elem in num_list]))
    
    comb3 = it.product(str(list_str), repeat=3)
    comb2 = it.product(str(list_str), repeat=2)

    digits3 = [(int(i), int(j), int(k)) for i, j, k in list(comb3)]
    digits2 = [(int(i), int(j)) for i, j in list(comb2)]
    
    print(len(digits3))
    print(len(digits2))
    for i in range(len(digits3)):
        for j in range(len(digits2)):
            num3 = convert(digits3[i])
            num2 = convert(digits2[j])
            product = num3 * num2
            p1 = num3 * int(str(num2)[0])
            p2 = num3 * int(str(num2)[1])
            if checkNum(product, num_list) and checkNum(p1, num_list) and \
                checkNum(p2, num_list) and len(str(p1)) == 3 and len(str(p2)) == 3:
                print("p", product)
                print("p1", p1)
                print("p2", p2)
                print("num3", num3)
                print("num2", num2)
                answer += 1
                
    return answer
    


def outputFile(answer):
    f = open("crypt1.out", mode = 'w')
    f.write(str(answer) + "\n")
    f.close()

if __name__ == "__main__":
    answer = main()
    outputFile(answer)
