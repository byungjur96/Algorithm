result = [1]*10

for _ in range(1, int(input())):
    for i in range(1, 10):
        result[i] = result[i-1]+result[i]
    
print(sum(result) % 10007)