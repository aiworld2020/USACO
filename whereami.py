import itertools as it

def findPattern(n, string):
    temp_length = n-1
    while temp_length > 1:
        temp_strings_list = []
        #start splitting string
        split = n - temp_length
        print("split = ", split)
        for i in range(split + 1):
            temp_strings_list.append(string[i:i+temp_length])
        print("temp strings")
        print(temp_strings_list)
        print("***")
        temp_length -= 1
        for i in range(len(temp_strings_list)):
            if temp_strings_list.count(temp_strings_list[i]) > 1:
                return len(temp_strings_list[i]) + 1

def main():
    answer = 0
    f = open("whereami.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    n = int(splitted[0])
    string = splitted[1]
    answer = findPattern(n, string)
    return answer

def outputFile(answer):
    f = open("whereami.out", mode = "w")
    f.write(str(answer) + "\n")

if __name__ == "__main__":
    answer = main()
    outputFile(answer)