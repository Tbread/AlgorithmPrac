import heapq
import copy

def solution(arr):
    arr2 = copy.deepcopy(arr)
    heapq.heapify(arr2)
    minnum = heapq.heappop(arr2)
    idx = arr.index(minnum)
    del arr[idx]
    return arr
