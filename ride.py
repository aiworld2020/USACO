"""
ID: aryanra2
LANG: PYTHON3
TASK: ride
"""

comet_name = ""
comet_numbers = []
group_name = ""
group_numbers = []
result = ""

#Split on \n
f = open("ride.in", mode = "r")
content = f.read()
splitted = content.split("\n")

def getCometName():
    comet_name = splitted[0]
    return comet_name



def getGroupName():
    group_name = splitted[1]
    return group_name


def changeToNumbers():
    for comet_letter in comet_name:
        comet_number = ord(comet_letter) - 64
        comet_numbers.append(comet_number)
    
    for group_letter in group_name:
        group_number = ord(group_letter) - 64
        group_numbers.append(group_number)



def checkRide(comet_numbers, group_numbers):
    comet_product = 1
    for x in comet_numbers:
        comet_product *= x
        
    group_product = 1
    for y in group_numbers:
        group_product *= y
    
    comet_product %= 47
    group_product %= 47
    
    if comet_product == group_product:
        result = "GO\n"
        return result
    else:
        result = "STAY\n"
        return result



def outputFile():
    with open("ride.out", mode = "w") as f:
        f.write(result)

comet_name = getCometName()
group_name = getGroupName()
changeToNumbers()
result = checkRide(comet_numbers, group_numbers)
outputFile()
