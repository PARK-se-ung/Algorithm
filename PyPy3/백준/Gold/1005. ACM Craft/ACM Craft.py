import sys
input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split(' '))
    craft = list(map(int, input().split(' ')))
    adj = [[] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2 = map(int, input().split(' '))
        adj[v2].append(v1)
    
    time = [-1 for _ in range(v + 1)]

    def tech(goal):
        if time[goal] > -1:
            return time[goal]
        if not adj[goal]:
            time[goal] = craft[goal - 1]
            return craft[goal - 1]
        current_time = craft[goal - 1]
        max_value = 0
        for build in adj[goal]:
            if time[build] == -1:
                time[build] = tech(build)
            if time[build] > max_value:
                max_value = time[build]
        time[goal] = current_time + max_value
        return current_time + max_value
    
    goal = int(input())
    print(tech(goal))
