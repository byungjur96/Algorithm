def bi_coder(n):
    temp = []
    while n > 0:
        temp.append(n%2)
        n = n//2
    return temp

def minus_bi(n):
    if n == 0:
        return "0"
    bi = bi_coder(abs(n))
    result = [0] * (len(bi)+3)
    
    for i in range(len(bi)):
        if bi[i] == 1:
            result[i]+=1
            if n > 0 and i % 2 == 1:
                result[i+1]+=1
            if n < 0 and i % 2 == 0:
                result[i+1]+=1
    for i in range(len(result)-2):
        if result[i] == 2:
            result[i] = 0
            if result[i+1] == 0:
                result[i+1]+=1
                result[i+2]+=1
            else:
                result[i+1]-=1

    result.reverse()
    while result[0] == 0:
        result = result[1:]
    return "".join(map(str, result))

n = int(input())
print(minus_bi(n))