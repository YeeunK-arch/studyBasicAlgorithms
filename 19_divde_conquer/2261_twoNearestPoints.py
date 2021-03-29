# the two nearest points [acmicpc : 2261]
# the recursive divide and conquer approach
import sys
R = sys.stdin.readline

def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def closetPair(left, right):
    # basic case
    if right - left <= 3:
        minDist = float('inf')
        for i in range(right-left):
            for j in range(i+1, right-left+1):
                currentDist = dist(dots[i], dots[j])
                if currentDist < minDist:
                    minDist = currentDist
        return minDist
    # recursion
    mid = (left + right) // 2
    minDist = min(closetPair(left, mid), closetPair(mid+1, right))




n = int(R())
dots = []
for _ in range(n):
    x, y = map(int, R().split())
    dots.append((x, y))
dots.sort(key=lambda d:d[0]) #x에 대해서만 정렬
closetPair(0, n - 1)