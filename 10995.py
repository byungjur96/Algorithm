n = int(input())
string = ""

for i in range(n):
    string += "*"
    if i != (n-1):
        string += " "

for i in range(n):
    if i % 2 == 1:
        print(" ", end="")
    print(string)
