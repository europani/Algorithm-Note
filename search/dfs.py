def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 노드 정보 2차원 리스트
graph = [
    [],
    [2, 3],
    [4, 5],
    [6, 7],
    [2],
    [2],
    [3],
    [3]
]

visited = [False] * 8   # 방문처리 리스트
dfs(graph, 1, visited)  # 1번 노드에서 시작