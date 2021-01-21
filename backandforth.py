import itertools as it

def main():
    f = open("backandforth.in", mode = "r")
    content = f.read()
    splitted = content.split("\n")
    
    array1 = set([int(x) for x in splitted[0].split(" ")])
    array2 = set([int(x) for x in splitted[1].split(" ")])
    
    
    
    comb1 = list(it.combinations_with_replacement(array1, 2))
    comb2 = list(it.combinations_with_replacement(array2, 2))
    
    print(len(comb1))
    print(len(comb2))

main()