"""
ID: aryanra2
LANG: PYTHON3
TASK: milk
"""

def sort(splitted):
    splitted.sort(key = lambda x:x[0])
    return splitted

def solve(amt_milk, max_farmers, data_list):
    milk_counter = 0
    cost = 0
    i = checkStart(amt_milk, max_farmers, data_list)
    print(i)
    while milk_counter < amt_milk:
        milk_counter += data_list[i][1]
        print(milk_counter)
        cost += data_list[i][0] * data_list[i][1]
        #print("cost = " + str(cost))
        i += 1
        
    if milk_counter > 100:
        extra_milk = milk_counter - amt_milk
        cost -= data_list[i-1][0] * extra_milk
    return cost

def checkStart(amt_milk, max_farmers, data_list):
    milk_counter = 0
    milk_list = list(map(lambda x: x[1], data_list))
    #print(milk_list)
    for i in range(max_farmers):
        total = sum(milk_list[i:max_farmers + i])
        if total >= amt_milk:
            return i
            
    
def main():
    f = open("milk.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    
    n = int(splitted[0].split(" ")[0])
    m = int(splitted[0].split(" ")[1])
    if m == 0 and n == 0:
        return 0
    del splitted[0]
    del splitted[-1]
    for i in range(len(splitted)):
        splitted[i] = splitted[i].split(" ")
        splitted[i] = int(splitted[i][0]), int(splitted[i][1])
       
    splitted = sort(splitted)
    cost = solve(n, m, splitted)
    return cost
 
def outputFile(cost):
    f = open("milk.out", mode = "w")
    f.write(str(cost) + "\n")
    
cost = main()
outputFile(cost)

