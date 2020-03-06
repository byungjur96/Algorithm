number = list(map(int, list(input())))
is_three = (sum(number) % 3 == 0)
is_ten = 0 in number
if is_three and is_ten:
    number.sort(reverse=True)
    print("".join(list(map(str, number))))
else:
    print(-1)
