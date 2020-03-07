import sys

heap = [None]
len_heap = 0


def min_heapify(i):
    global heap, len_heap
    left = 2 * i
    right = 2 * i + 1
    if right <= len_heap and heap[right] < heap[i]:
        smallest = right
    else:
        smallest = i

    if left <= len_heap and heap[left] < heap[smallest]:
        smallest = left

    if smallest != i:
        temp = heap[i]
        heap[i] = heap[smallest]
        heap[smallest] = temp
        min_heapify(smallest)


n = int(input())

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    # Pop
    if x == 0:
        # Heap이 비어있는 경우
        if len_heap == 0:
            print(0)
        # Heap에 값이 들어있는 경우
        else:
            print(heap[1])
            heap[1] = heap[len_heap]
            del heap[len_heap]
            len_heap -= 1
            min_heapify(1)

    # Insert
    else:
        len_heap += 1
        heap.append(x)
        if len_heap > 1:
            val = len_heap
            while val > 0:
                min_heapify(val)
                val = val // 2
