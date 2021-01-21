"""
ID: aryanra2
LANG: PYTHON3
TASK: beads
"""
n = 0
beads = []
beads_set = set()
bead_b = "b"
bead_r = "r"
bead_w = "w"
max_count = 0


f = open("beads.in", mode = "r")
content = f.read()
splitted = content.split("\n")

def getN():
    n = splitted[0]
    return int(n)

def getBeads():
    beads_string = splitted[1]
    for i in range(len(beads_string)):
        beads.append(beads_string[i])

def rearrangeBeads():
    #first_bead = beads[0]
    last_bead = beads[-1]
    
    for i in range(len(beads)):
        if beads[i] == bead_w:
            continue
        else:
            first_bead = beads[i]
            break
    
    if first_bead == bead_b:
        while last_bead != bead_r:
            beads.insert(0, last_bead)
            del beads[-1]
            last_bead = beads[-1]
            
    elif first_bead == bead_r:
        while last_bead != bead_b:
            beads.insert(0, last_bead)
            del beads[-1]
            last_bead = beads[-1]

def checkForEqual():
    beads_set = set(beads)
    if bead_r in beads_set and bead_b in beads_set:
        return False
    else:
        return True
    
    
def findMaxCount():
    i = 0
    max_count = 0
    blue_count = 0
    red_count = 0
    first_bead = beads[0]
    while i < n:
        if first_bead == bead_b:
            while beads[i] != bead_r:
                blue_count += 1
                i += 1
                if i >= n:
                    break
            while beads[i] != bead_b:
                red_count += 1
                i += 1
                if i >= n:
                    break
            if max_count < blue_count + red_count:
                max_count = red_count + blue_count
            blue_count = 0
            red_count = 0
          
        else:
            while beads[i] != bead_b:
                red_count += 1
                i += 1
                if i >= n:
                    break
            while beads[i] != bead_r:
                blue_count += 1
                i += 1
                if i >= n:
                    break
            if max_count < blue_count + red_count:
                max_count = red_count + blue_count
            blue_count = 0
            red_count = 0
       
    print("max count 1 = ", str(max_count))
    blue_count = 0
    red_count = 0
    if first_bead == bead_b:
        i = 0
        while beads[i] != bead_r:
            blue_count += 1
            i += 1
            if i >= n:
                break
        j = i
        i = -1
        while beads[i] != bead_b:
            red_count += 1
            i -= 1
            if abs(i) + j >= n:
                break
        if max_count < blue_count + red_count:
            max_count = red_count + blue_count
        blue_count = 0
        red_count = 0
        
    else:
        i = 0
        while beads[i] != bead_b:
            red_count += 1
            i += 1
            if i >= n:
                break
        j = i
        i = -1
        while beads[i] != bead_r:
            blue_count += 1
            i -= 1
            if abs(i) + j >= n:
                break
        if max_count < blue_count + red_count:
            max_count = red_count + blue_count
        blue_count = 0
        red_count = 0
    print("max count 2 = ", str(max_count))
    return max_count

def outputFile():
    with open("beads.out", mode = "w") as f:
        f.write(str(max_count) + "\n")
        

n = getN()
getBeads()
if checkForEqual():
    max_count = len(beads)
else:
    rearrangeBeads()
    max_count = findMaxCount()
outputFile()


