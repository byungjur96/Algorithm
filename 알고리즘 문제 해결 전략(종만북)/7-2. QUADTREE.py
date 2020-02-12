def reverse(string, pointer=0):
    if pointer > len(string):
        return ""

    if string[pointer] == 'b' or string[pointer] == 'w':
        return string[pointer]
    pointer += 1
    upper_left = reverse(string[pointer:])
    pointer += len(upper_left)
    upper_right = reverse(string[pointer:])
    pointer += len(upper_right)
    lower_left = reverse(string[pointer:])
    pointer += len(lower_left)
    lower_right = reverse(string[pointer:])
    print("x", lower_left, lower_right, upper_left, upper_right)
    return "x" + lower_left + lower_right + upper_left + upper_right


case = int(input())
for _ in range(case):
    line = input()
    print(reverse(line))
