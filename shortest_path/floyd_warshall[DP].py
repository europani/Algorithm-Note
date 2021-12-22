import sys

input=sys.stdin.readline
INF = sys.maxsize

# n: 노드갯수, m: 간선갯수
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n + 1)]  # 노드정보 무한대로 초기화

# 자기자신 경로 0 으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 모든 노드정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()