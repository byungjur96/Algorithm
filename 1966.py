import sys


def printer():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    documents = list(map(int, sys.stdin.readline().rstrip().split()))
    printed = 0

    while documents:
        is_first = True
        top_priority = documents[0]
        for i in range(1, n - printed):
            if documents[i] > top_priority:
                is_first = False
                break
        # 중요도가 가장 높을 떄
        if is_first:
            # 해당 문서 차례일 때
            if m == 0:
                return printed + 1
            # 일반 문서일 때: 출력하고 큐에서 뺀다.
            else:
                printed += 1
                del documents[0]
                m -= 1
        # 중요도가 가장 높은 문서가 뒤에 있을 떄
        else:
            if m == 0:
                m = n - printed - 1
            else:
                m -= 1
            documents.append(documents[0])
            del documents[0]


case = int(input())

for _ in range(case):
    print(printer())
