text = input()
cipher = ""

for t in text:
    if ord('a') <= ord(t) <= ord('z'):
        c = chr((ord(t) - ord('a') + 13) % 26 + ord('a'))
    elif ord('A') <= ord(t) <= ord('Z'):
        c = chr((ord(t) - ord('A') + 13) % 26 + ord('A'))
    else:
        c = t
    cipher += c

print(cipher)
