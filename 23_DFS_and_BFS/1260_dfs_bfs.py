from sys import stdin
R = stdin.readline
N, M, V = map(int, R().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, R().split())
    matrix[i][j] = matrix[j][i] = 1

def DFS(V, visited):
    visited += [V]
    for i in range(1, N+1):
        if matrix[V][i] == 1 and (i not in visited):
            DFS(i, visited)
    return visited

def BFS(V):
    visited = [V]
    que = [V]
    while que:
        p = que.pop(0)
        for i in range(1, N+1):
            if matrix[p][i] == 1 and (i not in visited):
                visited.append(i)
                que.append(i)
    return visited

print(*DFS(V, []))
print(*BFS(V))