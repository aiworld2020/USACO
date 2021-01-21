"""
ID: aryanra2
LANG: PYTHON3
TASK: skidesign
"""

def get17s(ski_hills):
    end_list = []
    for i in range(ski_hills[-1] - 16):
        end_list.append((i, i+17))
    return end_list
    

def main():
    answer = 9999999999999999
    f = open("skidesign.in", mode = "r")
    content = f.read()
    ski_hills = content.split("\n")
    
    n = int(ski_hills[0])
    del ski_hills[0]
    del ski_hills[-1]
    ski_hills = [int(x) for x in ski_hills]
    ski_hills.sort()
    pos_vals = get17s(ski_hills)
    current_cost = 0
    for i in range(len(pos_vals)):
        for j in range(len(ski_hills)):
            if ski_hills[j] < pos_vals[i][0]:
                current_cost += pow(pos_vals[i][0] - ski_hills[j], 2)
                
            elif ski_hills[j] > pos_vals[i][1]:
                current_cost += pow(ski_hills[j] - pos_vals[i][1], 2)
                
            else:
                current_cost += 0
        print(current_cost)
        if current_cost < answer:
            
            answer = current_cost
        current_cost = 0
    
    return answer

def outputFile(answer):
    f = open("skidesign.out", mode = "w")
    f.write(str(answer) + "\n")

if __name__ == "__main__":
    answer = main()
    outputFile(answer)