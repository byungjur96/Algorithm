self_num = [True for i in range(10000)]

for i in range(10000):
    string = str(i)
    num = i
    for s in string:
        num += int(s)
    if num < 10000:
        self_num[num-1] = False

for i in range(10000):
    if self_num[i] is True:
        print(i+1)
