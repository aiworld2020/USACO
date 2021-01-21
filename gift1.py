"""
ID: aryanra2
LANG: PYTHON3
TASK: gift1
"""

np = 0
ng = 0
names = []
money = []
splitted = []
def getNP():
    f = open("gift1.in", mode = "r")
    np = f.readline()
    f.close()
    return int(np, 0)


def getNames():
    f = open("gift1.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    i = 1
    while(i <= np):
        names.append(splitted[i])
        money.append(0)
        i += 1
    f.close()

def adjustBalances():
    i = np + 1
    f = open("gift1.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    print("length of splitted = ", len(splitted))
    while i < (len(splitted) - 1):
        print(i)
        giver = splitted[i]
        i += 1
        givingDetails = splitted[i]
        print("giver: ", giver)
        #print("details: ", givingDetails)
        
        
        amount = int(givingDetails.split(" ")[0])
        numberOfPeople = int(givingDetails.split(" ")[1])
        t_idx_giver = names.index(giver)
        money[t_idx_giver] -= amount
        if numberOfPeople != 0:
            money[t_idx_giver] += amount % numberOfPeople
        
        #print("amount: ", amount)
        #print("people", numberOfPeople)
        count = 0
        while count < numberOfPeople:
            t_name = splitted[i + 1 + count]
            t_idx = names.index(t_name)
            money[t_idx] += int(amount / numberOfPeople)
            count += 1
        i += numberOfPeople + 1
        # print(money)   
        # print("file counter: ", i)




def outputFile():
    with open("gift1.out", mode = "w") as f:
        for i in range(len(names)):
            f.write(names[i] + " " + str(money[i]) + "\n")
    



np = getNP()
getNames()
adjustBalances()
outputFile()


