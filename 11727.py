solutions = [1, 3]

length = int(input())

for i in range(2, length):
    solution = solutions[i-1] + solutions[i-2] * 2
    solutions.append(solution)

print(solutions[length-1] % 10007)
