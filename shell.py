def swapAndCheck(pebble,shell_list, n):
    t_answer = 0
    shell_order = [1,2,3]
    for i in range(n):
        swap1 = shell_list[i][0] - 1
        swap2 = shell_list[i][1] - 1
        int1 = shell_order[swap1]
        int2 = shell_order[swap2]
        shell_order[swap2] = int1
        shell_order[swap1] = int2
        if shell_order.index(pebble) == shell_list[i][2] - 1:
            
            t_answer += 1
    return t_answer


def main():
    f = open("shell.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    
    n = int(splitted[0])
    shell_list = splitted[1:n+1]
    
    for i in range(len(shell_list)):
        shell_list[i] = shell_list[i].split(" ")
        for j in range(3):
            shell_list[i][j] = int(shell_list[i][j])
    
    shell_order = [1,2,3]
    answer = 0
    for i in range(3):
        pebble = shell_order[i]
        t_answer = swapAndCheck(pebble, shell_list, n)
        if t_answer > answer:
            answer = t_answer
    return answer
    
def outputFile(answer):
    f = open("shell.out", mode = "w")
    f.write(str(answer) + "\n")

if __name__ == "__main__":
    answer = main()
    outputFile(answer)