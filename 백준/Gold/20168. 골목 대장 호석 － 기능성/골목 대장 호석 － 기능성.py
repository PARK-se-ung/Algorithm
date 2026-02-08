import sys
input = sys.stdin.readline

# 백트래킹을 활용한 완전 탐색
def find(v, adj, start, end, money):

    # 재방문 방지를 위한 방문처리
    visited = [False] * v
    visited[start] = True

    # 시작 지점에서 도착 지점까지 갈 수 있는 모든 경로에서의 요금의 최댓값들의 배열
    result = []

    # 백트래킹
    def back(current, end, total, limit, max_value):
        # 도착 경로일 때의 최대 요금
        if current == end:
            result.append(max_value)
        
        for cost, next in adj[current]:
            # 다음 노드를 방문 가능하고 방문하지 않았으면
            if total + cost <= limit and not visited[next]:
                # 방문처리후 백트래킹
                visited[next] = True
                back(next, end, total + cost, limit, max(max_value, cost))
                visited[next] = False

    back(start, end, 0, money, 0)

    # 가능한 경로가 없으면
    if not result:
        return -1
    
    # 가능한 경로 중 최소
    return min(result)


v, e, start, end, money = map(int, input().split())
start, end = start - 1, end - 1
adj = [[] for _ in range(v)]
for _ in range(e):
    v1, v2, cost = map(int, input().split())
    adj[v1 - 1].append((cost, v2 - 1))
    adj[v2 - 1].append((cost, v1 - 1))

print(find(v, adj, start, end, money))