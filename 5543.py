price = []

for _ in range(5):
    price.append(int(input()))

burger = price[:3]
juice = price[3:]

burger_pic = burger[0]
for b in burger:
    if b < burger_pic:
        burger_pic = b


if juice[1] > juice[0]:
    juice_pic = juice[0]
else:
    juice_pic = juice[1]

print(juice_pic + burger_pic - 50)
