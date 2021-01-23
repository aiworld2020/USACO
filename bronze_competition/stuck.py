"""
ID: aryanra2
LANG: PYTHON3
TASK: stuck
"""
import sys

n = 0
cow_pos = []
cow_dir = []
farm = []
cow_moves = []
cow_stopped = []


def main():
    size = 1000

    cows = sys.stdin.readlines()
    n = int(cows[0])
    del cows[0]
    cow_dir = [cows[i].split(" ")[0] for i in range(len(cows))]
    cow_pos = [(int(cows[i].split(" ")[1]), int(cows[i].split(" ")[2]))  for i in range(len(cows))]
    
    # f = open("p3.in", mode = "r")
    # content = f.read()
    # cows = content.split("\n")
    # #cows = sys.stdin.readlines()
    # n = int(cows[0])
    # del cows[0]
    # cow_dir = [cows[i].split(" ")[0] for i in range(len(cows))]
    # cow_pos = [(int(cows[i].split(" ")[1]), int(cows[i].split(" ")[2]))  for i in range(len(cows))]
    # print("Cow Direction ", cow_dir)
    # print("Cow Position", cow_pos)
    
    t_x = [i[0] for i in cow_pos]
    t_y = [i[1] for i in cow_pos]

    max_x = max(t_x)
    max_y = max(t_y)
    
    if(max_x > max_y):
        size = max_x + 1
    else:
        size = max_y + 1

    cow_moves = [0 for i in range(n)]
    #cow_stopped = [-1 for i in range(n)]
    is_cow_stopped = [0 for i in range(n)]
    field = [[0]*(size+1) for i in range(size+1)]
    iterations = size
    if (size > 1000):
        iterations = 1000
    for moves in range(iterations):
        for i in range(n):
            if (is_cow_stopped[i] == 1):
                continue
            direction = cow_dir[i]
            x = cow_pos[i][0]
            y = cow_pos[i][1]
            field[x][y] = 1
            cow_moves[i] = cow_moves[i] + 1
            if (direction  == 'E'):
                x = x + 1
            elif (direction == 'N'):
                y = y + 1
            #print("Position ", x, ",", y)
            if (x == size) or (y == size):
                cow_moves[i] = size
                is_cow_stopped[i] = 1
                continue
            if (field[x][y] == 1):
                is_cow_stopped[i] = 1
            else:
                cow_pos[i]=(x, y)
        for i in range(n):
            if (is_cow_stopped[i] == 1):
                continue
            direction = cow_dir[i]
            x = cow_pos[i][0]
            y = cow_pos[i][1]
            if (field[x][y] == 1):
                is_cow_stopped[i] = 1
        
        t_sum = sum(is_cow_stopped)
        if(t_sum  == n):
            break
        
    return n, size, iterations, cow_moves            
            
def outputFile(n, size, iterations, answer):
    for i in range(n):
        if answer[i] >= iterations:
            print("Infinity")
        else:
            print(answer[i])


if __name__ == "__main__":
    n, size, iterations, answer = main()
    outputFile(n, size, iterations, answer)