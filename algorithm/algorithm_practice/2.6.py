# 10769
happy = ':-)'
sad = ':-('
sentence = input()

if happy not in sentence and sad not in sentence:
    print('none')
elif sentence.count(happy) == sentence.count(sad):
    print('unsure')
elif sentence.count(happy) > sentence.count(sad):
    print('happy')
elif sentence.count(happy) < sentence.count(sad):
    print('sad')   

# 2455
cnt = 0
ls = []

for _ in range(4):
    a, b = list(map(int, input().split()))
    cnt = cnt - a + b
    ls.append(cnt)
print(max(ls))

# 2606

# def pprint(a):
#     for i in a:
#         print(i)

N = int(input())
t = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for _ in range(t):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# pprint(graph)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()

        for i in graph[cur]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    
    # print(visited)
    print(visited.count(True) - 1)
dfs(1)



# > 스택은 노드를 쌓아놓는 것. 현재 pop은 최상단노드.
# mlp에서 true는 값을 탐색했음을 의미하지는 않는거 같다. 그냥 관계를 맺은 적이 있는지 나타냄.(간선)
# 관계를 맺은 적이 있다는것은(true),
# dfs 방문순서나 스택 순서는 문제에 따라 중요하기도 하지만 중요하지 않다.
# 중요한건 '한 방향'으로 '모든 노드를 탐색했는지'이다.