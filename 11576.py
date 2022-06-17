def a_to_dec(lst, a):
    mul = 1
    result = 0
    while lst:
        result += (lst.pop() * mul)
        mul *= a
    return result

def dec_to_b(n, b):
    result = []
    while n > 0:
        result.append(n % b)
        n = n // b
    result.reverse()
    return result


a, b = map(int, input().split())
m = int(input())
a_val = list(map(int, input().split()))
print(" ".join(map(str, dec_to_b(a_to_dec(a_val, a), b))))