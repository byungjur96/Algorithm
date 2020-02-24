word = input()
new_word = ""

for w in word:
    if ord('a') <= ord(w) <= ord('z'):
        new_word += chr(ord(w) + ord('A') - ord('a'))
    else:
        new_word += chr(ord(w) - ord('A') + ord('a'))

print(new_word)
