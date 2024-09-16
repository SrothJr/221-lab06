#...Solve the problem by figuring all possible paths 

def dfs(u,w, d, visited, path):
    visited[u] = True
    path.append((u, w))

    if u == d:
        result.append(path.copy())
    else:
        for node, weight in adj[u]:
            if visited[node] == False:
               dfs(node, weight, d, visited, path)

    path.pop()
    visited[u] = False

input_file = open("input/input03_brute.txt", "r")
output_file = open("output/output03_brute.txt", "w")

n, m = [int(i) for i in input_file.readline().strip().split(" ")]

edges = []
for i in range(m):
    edges.append([int(i) for i in input_file.readline().strip().split(" ")])

# print(edges)
adj = {}
for i in range(1, n):
    adj[i] = []
for i in edges:
    adj[i[0]].append([i[1], i[2]])

# print(adj)

visited = [False] * (n+1)
# print(visited)
result = []
dfs(1,0, n, visited, [])
# print(result)

path_max = []
for i in result:
    all_weight = []
    for j in i:
        all_weight.append(j[1])
    path_max.append(max(all_weight))

print(min(path_max), file= output_file)
output_file.close()
