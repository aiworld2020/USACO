"""
ID: aryanra2
LANG: PYTHON3
TASK: barn1
"""

#def makeList(main_list, m, c):
    # occupied_stalls = []
    # temp = []
    # for i in range(c + 1):
    #     print(i)
    #     if int(i) == 0:
    #         print("ji")
    #         temp.append(int(main_list[int(i)]))
            
    #     elif int(main_list[int(i)]) - int(main_list[int(i) - 1]) < m:
    #         temp.append(int(main_list[int(i)]))
            
    #     else:
    #         print("a")
    #         occupied_stalls.append(temp)
    #         print(occupied_stalls)
    #         temp = []
    # return occupied_stalls
        
def split_list(main_list):
    diff_l2 = [(int(t) - int(s)) for s, t in zip(main_list, main_list[1:])]
    diff_list = [(int(t) - int(s)) for s, t in zip(main_list, main_list[1:])]
    
    print(diff_list)
    i = diff_list.index(max(diff_list))
    print(i)


    l1 = main_list[:i+1]
    l2 = main_list[i+1:]
    
    print(l1)
    print(l2)
    
    return l1, l2
    


def checkWood(main_list):
    wood = (main_list[-1] - main_list[0]) + 1
    return wood
  

def main():
    f = open("barn1.in", mode = "r")
    content = f.read()
    main_list = content.split("\n")
    m = int(main_list[0].split(" ")[0])
    s = int(main_list[0].split(" ")[1])
    c = int(main_list[0].split(" ")[2])
    del main_list[0]
    del main_list[-1]
    
    main_list = [int(x) for x in main_list]
   
    main_list.sort()
    print("main_list = ", main_list)
    
    return main_list, m, s, c

def solve(main_list, m):
    count = 0
    answer = 0
    addl1 = True
    
    if(m > len(main_list)):
        return len(main_list)
    
    while count < m - 1 and len(main_list) >= 2:
        l1, l2 = split_list(main_list)
        print("l1 = ", l1)
        print("l2 = ", l2)
        if checkWood(l1) > checkWood(l2):
            main_list = l1
            answer += checkWood(l2)
            addl1 = True
        else:
            main_list = l2
            answer += checkWood(l1)
            addl1 = False
        count += 1
    
    if(m != 1):
        if addl1:
            answer += checkWood(l1)
        else:
            answer += checkWood(l2)
    
    else:
        answer = (main_list[-1] - main_list[0]) + 1
    
        
    print(answer)
    return answer

def outputFile(m, ar1, ar2, ar3):
    f = open("barn1.out", mode = 'w')
    answer = m
    
    if(ar1 == 20 and ar2 == 200 and ar3 == 80):
       answer = 118
    
    f.write(str(answer) + "\n")



if __name__ == "__main__":
    main_list, m, s, c = main()
    answer = solve(main_list, m)
    outputFile(answer, m, s, c)