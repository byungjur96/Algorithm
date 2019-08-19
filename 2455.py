max_people = 0
current_people = 0
for _ in range(4):
    hopOut, hopIn = map(int, input().split())
    current_people -= hopOut
    current_people += hopIn
    if max_people < current_people:
        max_people = current_people
print(max_people)
