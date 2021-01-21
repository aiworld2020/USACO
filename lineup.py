import itertools as it

def checkList(poss_sol, constraints, n):
    for i in range(n):
        cow1 = constraints[i][0]
        cow2 = constraints[i][1]
        index1 = poss_sol.index(cow1)
        index2 = poss_sol.index(cow2)
        if abs(index1 - index2) != 1:
            return False
    return True
    
    

def main():
    constraints = []
    names = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue", "Buttercup", "Sue"]
    f = open("lineup.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    
    n = int(splitted[0])
    del splitted[0]
    constraints = [(splitted[i].split(" ")[-1], splitted[i].split(" ")[0]) for i in range(n)]
    constraints.sort(key = lambda x:x[1])
    
    all_comb = list(it.permutations(names, len(names)))
    for i in range(len(all_comb)):
        poss_sol = all_comb[i]
        if checkList(poss_sol, constraints, n):
            return poss_sol

def outputFile(answer):
    f = open("lineup.out", mode = "w")
    for i in range(len(answer)):
        f.write(answer[i] + "\n")

if __name__ == "__main__":
    answer = main()
    outputFile(answer)

