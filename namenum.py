"""
ID: aryanra2
LANG: PYTHON3
TASK: namenum
"""
n = ""
possible_names_dict = {}
possible_names_list = []
f = open("dict.txt", mode = "r")
content = f.read()
valid_names = content.split("\n")

def getN():
    f = open("namenum.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    n = splitted[0]
    return n



def makeDict():
    for i in range(len(n)):
        if n[i] == "2":
            possible_names_dict["2"] = ["A", "B", "C"]
        elif n[i] == "3":
            possible_names_dict["3"] = ["D", "E", "F"]
        elif n[i] == "4":
            possible_names_dict["4"] = ["G", "H", "I"]
        elif n[i] == "5":
            possible_names_dict["5"] = ["J", "K", "L"]
        elif n[i] == "6":
            possible_names_dict["6"] = ["M", "N", "O"]
        elif n[i] == "7":
            possible_names_dict["7"] = ["P", "R", "S"]
        elif n[i] == "8":
            possible_names_dict["8"] = ["T", "U", "V"]
        elif n[i] == "9":
            possible_names_dict["9"] = ["W", "X", "Y"]

def getPossibleNames():
    for name in valid_names:
        if len(name) != len(n):
            continue
        else:
            i = 0
            while i < len(n):
                if name[i] == possible_names_dict[n[i]][0] or \
                name[i] == possible_names_dict[n[i]][1] or \
                name[i] == possible_names_dict[n[i]][2]:
                    if i == len(n) - 1:
                        possible_names_list.append(name)
                    i += 1
                else:
                    break

def outputFile():
    with open("namenum.out", mode = "w") as f:
        if len(possible_names_list) == 0:
            f.write("NONE\n")
        else:
            for i in range(len(possible_names_list)):
                f.write(possible_names_list[i] + "\n")
n = getN()
makeDict()
getPossibleNames()
outputFile()



