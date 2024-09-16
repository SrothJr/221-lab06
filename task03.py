import heapq as hq

def dijkstra_min_max(graph, start, end, n):
    # Initialize distances with infinity
    distances = {node: float('infinity') for node in range(1, n + 1)}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_max_danger, current_node = hq.heappop(priority_queue)
        
        if current_node == end:
            return current_max_danger
        
        for neighbor, danger in graph[current_node]:
            max_danger = max(current_max_danger, danger)
            if max_danger < distances[neighbor]:
                distances[neighbor] = max_danger
                hq.heappush(priority_queue, (max_danger, neighbor))
    
    return "Impossible"

def solve_safest_path(n, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, k in edges:
        graph[u].append((v, k))
        # graph[v].append((u, k))  # Assuming undirected graph
    # print(graph)
    return dijkstra_min_max(graph, 1, n, n)

input_file = open("input/input03.txt", "r")
output_file = open("output/output03.txt", "w")


n, m = [int(i) for i in input_file.readline().strip().split(" ")]
edges = []
for i in range(m):   #....The lab stask starts from 1
    edges.append([int(i) for i in input_file.readline().strip().split(" ")])

# print(edges)

result = solve_safest_path(n, edges)
print(result, file= output_file)
output_file.close()  
