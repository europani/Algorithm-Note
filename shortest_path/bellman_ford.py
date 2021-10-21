import sys

input = sys.stdin.readline
INF = int(1e9)      # 10억

# n: 노드갯수, m: 간선갯수
n, m = map(int, input().split())
graph = []                          # 노드정보
distance = [INF] * (n+1)            # 최단경로

# 모든 노드정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

# 벨만 포드 알고리즘
def bf(start):
    # 시작노드 초기화
    distance[start] = 0

    for i in range(n):      # 노드 갯수만큼 round 진행
        for j in range(m):  # 해당 노드의 모든 간선 확인
            cur = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]

            # 현재 노드를 거쳐 다른 연결된 노드로 이동하는 거리가 짧은 경우
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost

                if i == n-1:    # n번째 라운드에도 값이 갱신된다면 음수 순환이 존재
                    return True
    return False


negative_cycle = bf(1)      #  1번 노드에서 시작

# 결과 출력
if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if distance[i] == INF:  # 도달할 수 없는 경우
            print("-1")
        else:                   # 도달할 수 있는 경우
            print(distance[i])