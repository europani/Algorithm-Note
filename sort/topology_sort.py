from collections import deque

# n: 노드갯수, m: 간선갯수
n, m = map(int, input().split())
# 진입차수 리스트
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

# 모든 노드정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1      # 진입차수 1증가

def topology_sort():
    result = []
    q = deque()

    # 진입차수 0인 노드 큐에 삽입하여 초기화
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        # 현재 노드와 연결된 노드들의 진입차수 -1
        for i in graph[now]:
            indegree[i]-=1
            # 새롭게 진입차수가 0인 노드 큐에 삽입
            if indegree[i]==0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()