test = int(input())

for _ in range(test):
    total, sibling = map(int, input().split())
    each_sibling = total // sibling
    dad = total % sibling
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(each_sibling, dad))
