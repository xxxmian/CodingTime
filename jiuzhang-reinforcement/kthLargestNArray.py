def kthLargestNArray(arrays, k):
    import heapq
    heap = []
    n = len(arrays)

    for i in range(n):
        heapq.heappush(heap, (arrays[i][0], i, 0))

    ik = 0
    while heap:
        t = heapq.heappop(heap)
        ik += 1
        if ik == k:
            return t[0]
        if t[2]+1 < len(arrays[t[1]]):
            heapq.heappush(heap, (arrays[t[1]][t[2]+1], t[1], t[2]+1))

print(kthLargestNArray([[1,5],[10],[12,13,15]], 4))

