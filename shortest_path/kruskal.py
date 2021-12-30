# 특정 원소(x)가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때 까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소(a, b)가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:       # 작은 원소가 부모 원소
        parent[b] = a
    else:
        parent[a] = b

n, m= map(int, input().split())
parent = [0] * (n + 1)          # 부모 테이블 : 각 원소의 부모 원소번호 저장
edges = []                      # 간선정보

result = 0

# 각 원소가 부모를 자기자신으로 초기화
for i in range(1, n+1):
    parent[i] = i               

# 모든 간선정보 입력
for _ in range(m):
    a, b, cost = map(int, input().split())
    # cost로 정렬하기 위해 첫번째 위치
    edges.append((cost, a, b))

# cost순 정렬
edges.sort()


# 크루스칼 알고리즘
for edge in edges:
    cost, a, b = edge

    # 사이클이 발생하지 않을 경우만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)