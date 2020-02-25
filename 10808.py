alphabet = [0 for i in range(26)]

word = input()

for w in word:
    alphabet[ord(w) - ord('a')] += 1

print(" ".join(list(map(str, alphabet))))
