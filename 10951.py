while True:
    try:
        line = input()
        if len(line) == 3:
            print(int(line[0]) + int(line[2]))

    except EOFError:
        break
