import sys

heap = [None]
len_heap = 0


def max_heapify(i):
    global heap, len_heap
    left = 2 * i
    right = 2 * i + 1
    if right <= len_heap and heap[right] > heap[i]:
        largest = right
    else:
        largest = i

    if left <= len_heap and heap[left] > heap[largest]:
        largest = left

    if largest != i:
        temp = heap[i]
        heap[i] = heap[largest]
        heap[largest] = temp
        max_heapify(largest)


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
            max_heapify(1)

    # Insert
    else:
        len_heap += 1
        heap.append(x)
        if len_heap > 1:
            val = len_heap
            while val > 0:
                max_heapify(val)
                val = val // 2
