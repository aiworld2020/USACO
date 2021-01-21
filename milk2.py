"""
ID: aryanra2
LANG: PYTHON3
TASK: milk2
"""

n = 0
milking_done = 0
milking_not_done = 0
f = open("milk2.in", mode = "r")
content = f.read()
splitted = content.split("\n")
t_start_list = []
t_end_list = []
t_list = []

    

def getN():
    n = splitted[0]
    return int(n)

def rearrange():
    #create a list of tuples [(start1,end1), (start2, end2)]
    for i in range(1,n + 1):
        t_list.append((int(splitted[i].split(" ")[0]),(int(splitted[i].split(" ")[1]))))
    
    #sorts the list based on first value in tuple
    t_list.sort(key = lambda x:x[0])
    
    
    for i in range(n):
        t_start_list.append(t_list[i][0])
        t_end_list.append(t_list[i][1])
        
#    with open("milk2_big.in", mode = "w") as f:
#         for i in range(len(t_list)):
#              f.write(str(t_list[i][0]) + " " + str(t_list[i][1]) + "\n")

        
    #print(t_start_list)
    #print(t_end_list)


def getMilkingDone():
    #Iterate 1st time
    #create a new list such that the start and end times 
    #don't overlap
    #Iterate 2nd time
    #store the difference in another list and return max from this
    new_list = []
    start_num, end_num  = t_list[0]
    new_list.append(end_num - start_num)
    for i in range(1, len(t_list)):
        next_start_num, next_end_num  = t_list[i]
        if next_end_num < end_num:
            continue
        #next timings are in the middle
        elif next_end_num >= end_num and next_start_num <= end_num:
            end_num =  next_end_num
            new_list.append(end_num - start_num)
            continue
        
        else:
            #print("i = ", i, "start_num = ", start_num, "end_num =", end_num)
            
            start_num = next_start_num
            end_num = next_end_num
            #print("i = ", i, "start_num = ", start_num, "end_num =", end_num)
            
            new_list.append(end_num - start_num)
            
            
    return new_list
def getMilkingNotDone():
    i = 0
    old_farmer_end = 0
    milking_not_done = 0
    count = 0
    while i < n:
        if i >= 1:
            farmer_start = t_start_list[i]
            farmer_end = t_end_list[i]
            if farmer_end >= old_farmer_end:
                count = farmer_start - old_farmer_end
                old_farmer_end = farmer_end
            if count > milking_not_done:
                milking_not_done = count
            i += 1
            
        
        else:
            old_farmer_end = t_end_list[i]
            i += 1

    return milking_not_done

def outputFile():
    with open("milk2.out", mode = "w") as f:
        f.write(str(milking_done) + " " + str(milking_not_done) + "\n")
        
def tempoutputFile():
    with open("milk2big.in", mode = "w") as f:
        f.write(str(milking_done) + " " + str(milking_not_done) + "\n")
        
        
n = getN()
rearrange()

milking_done = max(getMilkingDone())
milking_not_done = getMilkingNotDone()
outputFile()





