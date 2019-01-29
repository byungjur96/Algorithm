line_len = int(input())

line_len = int(line_len/3)

init_square = ["*", "* *", "*****"]
result = ["  *  ", " * * ", "*****"]


# 입력받은 삼각형보다 2배 큰 삼각형을 만든다.
def next_triangle(before):
    res = before + before
    blank = ""
    before_len = len(before)

    for _ in range(before_len):
        blank += " "

    for i in range(before_len):
        res[before_len + i] = res[i] + " " + res[i]

        res[i] = blank + res[i] + blank

    return res


while line_len > 1:
    result = next_triangle(result)
    line_len /= 2

for r in result:
    print(r)
