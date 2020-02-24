count = 0
mo = ['a', 'e', 'i', 'o', 'u']
word = input()
for w in word:
    for m in mo:
        if w == m:
            count += 1

print(count)
