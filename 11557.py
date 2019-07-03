test_case = int(input())
maximum = 0
school = ''
for _ in range(test_case):
    school_num = int(input())
    for _ in range(school_num):
        name, alcohol = input().split()
        alcohol = int(alcohol)
        if alcohol > maximum:
            maximum = alcohol
            school = name
    print(school)
