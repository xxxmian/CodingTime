def KthSmallestSumInTwoSortedArrays(arr1, arr2, k):
    import heapq
    heap = []
    heapq.heappush(heap, (arr1[0]+arr2[0], 0, 0))
    ik = 0
    while heap:
        t = heapq.heappop(heap)
        ik += 1
        if ik == k:
            return t[0]
        if t[1]+1 < len(arr1):
            heapq.heappush(heap, (arr1[t[1]+1]+arr2[t[2]], t[1]+1, t[2]))
        if t[2]+1 < len(arr2):
            heapq.heappush(heap, (arr1[t[1]]+arr2[t[2]+1], t[1], t[2]+1))
print(KthSmallestSumInTwoSortedArrays([1,1.5,3],[1,4,6],5))
