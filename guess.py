def getAnswer(animals, n):
    k = 1
    answer = 0
    t = 0
    for i in range(n - 1):
        for j in range(2, len(animals[i])):
            if k <= i:
                k = i + 1
            if animals[i][j] in animals[k]:
                t += 1
            if t > answer:
                answer = t
                t = 0
            if k == n - 1:
                k = 0
            else:
                k += 1
    return answer + 1


def main():
    f = open("guess.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    n = int(splitted[0])
    animals = [i.split(" ") for i in splitted[1:n + 1]]
    answer = getAnswer(animals, n)
    return answer
    
def outputFile(answer):
    f = open("guess.out", mode = "w")
    f.write(str(answer) + "\n")

if __name__ == "__main__":
    answer = main()
    outputFile(answer)
