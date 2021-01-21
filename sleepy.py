def changeOrder(n, order, answer_list):
    answer = 0
    i = 0
    while True:
        if order == answer_list:
            answer = i
            break
        
        if order[0] == 1:
            max_num = max(order)
            ind = order.index(max_num)
            del order[0]
            order.insert(ind, 1)
        else:
            ind = order.index(order[0] - 1)
            order.insert(ind + 1, order[0])
            del order[0]
           # print(order, "\n")
        i += 1      
                     
    return answer            
                

def main():
    f = open("sleepy.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    
    n = int(splitted[0])
    order = [int(x) for x in splitted[1].split(" ")]
    answer_list = []
    for i in range(1, n + 1):
        answer_list.append(i)
    answer = changeOrder(n, order, answer_list)
    return answer

def outputFile(answer):
    f = open("sleepy.out", mode = "w")
    f.write(str(answer) + "\n")

if __name__ == "__main__":
    answer = main()
    outputFile(answer)

