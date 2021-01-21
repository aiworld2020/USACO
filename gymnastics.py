def getPairs(cow_ranks, n, k):
    poss_pairs = []
    for x in range(k):
        cow_line = cow_ranks[x]
        print(cow_line)
        for i in range(n - 1):
            for j in range(i + 1, n):
                poss_pairs.append((int(cow_line[i]), int(cow_line[j])))
    return poss_pairs
            
def reversePairs(poss_pairs):
    reverse_list = []
    reverse_list = [(poss_pairs[i][1], poss_pairs[i][0]) for i in range(len(poss_pairs))]
    print(reverse_list)
    return reverse_list

def main():
    poss_pairs = []
    reverse_list = []
    f = open("gymnastics.in", mode = "r")
    content = f.read()
    cow_ranks = content.split("\n")
    k = int(cow_ranks[0].split(" ")[0])
    n = int(cow_ranks[0].split(" ")[1])
    del cow_ranks[0], cow_ranks[-1]
    cow_ranks = [cow_ranks[i].split(" ") for i in range(len(cow_ranks))]
    poss_pairs = getPairs(cow_ranks, n, k)
    poss_pairs = list(set(poss_pairs))
    reverse_list = [(poss_pairs[i][1], poss_pairs[i][0]) for i in range(len(poss_pairs))]
    for i in reverse_list:
        if i in poss_pairs:
            poss_pairs.remove(i)
            poss_pairs.remove((i[1], i[0]))
    print(poss_pairs)
    return len(poss_pairs)

def outputFile(answer):
    f = open("gymnastics.out", mode = "w")
    f.write(str(answer) + "\n")

if __name__ == "__main__":
    answer = main()
    outputFile(answer)