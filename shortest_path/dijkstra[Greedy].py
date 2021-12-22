import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

# n: 노드갯수, m: 간선갯수
n, m = map(int, input().split())
# 시작 노드 번호
start = int(input())
graph = [[] for i in range(n + 1)]  # 노드정보
distance = [INF] * (n+1)            # 최단경로

# 모든 노드정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []

    # 시작노드 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 최단 경로 노드 선택
        dist, now = heapq.heappop(q)    # now : 현재 노드번호
        # 현재 노드가 이미 처리된 적이 있다면 무시 (힙에서 얻은 거리(dist)가 현재최단거리 보다 크다는 것은 이미처리 된 것)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]          # 현재 노드를 거쳐 다른 연결된 노드로 이동하는 거리
            if cost < distance[i[0]]:
                distance[i[0]] = cost   # 최단거리 갱신
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 결과 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
        
        