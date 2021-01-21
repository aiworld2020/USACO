def splitSentences(n, k, words):
    answer = []
    sentence = []
    previous_length = 0
    for i in range(n):
        if len(words[i]) + previous_length <= k:
            sentence.append(words[i])
            
        else:
            answer.append(sentence)
            sentence = []
            previous_length = 0
            sentence.append(words[i])
        previous_length += len(words[i])
        if i == n - 1:
            answer.append(sentence)
    return answer


def main():
    f = open("word.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    n = int(splitted[0].split(" ")[0])
    k = int(splitted[0].split(" ")[1])
    words = splitted[1].split(" ")
    #print(words)
    answer = splitSentences(n, k, words)
    return answer

def outputFile(answer):
    f = open("word.out", mode = "w")
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if j == len(answer[i]) - 1:
                f.write(answer[i][j] + "\n")
            else:
                f.write(answer[i][j] + " ")

if __name__ == "__main__":
    answer = main()
    outputFile(answer)