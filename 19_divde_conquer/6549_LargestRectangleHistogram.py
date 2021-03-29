#Largest Rectangle in a Histogram
from math import ceil, log2
import sys
sys.setrecursionlimit(10**6)
R = sys.stdin.readline

def init(start, end, node):
    if start == end:
        tree[node] = L[start], start # 높이를 저장해야하는데, 이때 인덱스도 함께 저장
    else:
        mid = (start + end) // 2
        tree[node] = min(init(start, mid, node*2), init(mid+1, end, node*2+1))
    return tree[node]

# return : (min, idx)
def minH(start, end, left, right, node):
    if left <= start and end <= right:
        return tree[node]
    elif end < left or right < start:
        return 1000000001, 0
    else:
        mid = (start + end) // 2
        return min(minH(start, mid, left, right, node*2), minH(mid+1, end, left, right, node*2 + 1))

def maxArea(start, end):
    if start > end :
        return 0
    elif start == end:
        return L[start]
    high, idx = minH(1, n, start, end, 1)
    return max(maxArea(start, idx-1), maxArea(idx+1, end), (end-start+1)*high)


while True:
    L = list(map(int, R().split()))
    if L[0] == 0:
        break
    else:
        n = L[0]
    # tree h = int(ceil(log2(n)))
    # tree size = 2 ** (h+1)
    # if idx start with 1, idx's children are idx*2, idx*2+1
    # make a tree
    size = 2 ** (ceil(log2(n) + 1))
    tree = [0 for _ in range(size)]
    init(1, n, 1)
    print(maxArea(1, n))
    # print(tree[1:])