def checkAperm(poss_a_perm, n):
    if min(poss_a_perm) <= 0:
        return False
    for i in range(n):
        if poss_a_perm.count(poss_a_perm[i]) == 1:
            continue
        else:
            return False
    return True


def main():
    f = open("photo.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    del splitted[-1]
    
    n = int(splitted[0])
    b_perm = [int(x) for x in splitted[1].split(" ")]
    
    
    for i in range(1, n + 1):
        poss_a_perm = []
        poss_a_perm.append(i)
        subtract = i
        for j in range(1, n):
            poss_a_perm.append(b_perm[j - 1] - subtract)
            subtract = poss_a_perm[j]
        if checkAperm(poss_a_perm, n):
            return poss_a_perm
    
  
def outputFile(answer):
    f = open("photo.out", mode = "w")
    for i in answer:
        if i == answer[len(answer) - 1]:
            f.write(str(i) + "\n")
        else:
            f.write(str(i) + " ")




if __name__ == "__main__":
    answer = main()
    outputFile(answer)

