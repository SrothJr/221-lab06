# Dijkstra's algorithm
import heapq as hq
#..Using heap queue cause it's a greedy method 

def djs(src, adj):
    n = len(adj)
    pq = []
    hq.heappush(pq, (0, src))  #..Pushing the source and it's weight which is zero.

    distance = [float("inf")] * n #...List to store distance, initially all nodes have infinity value.
    distance[src] = 0

    while pq:
        current_distance, u = hq.heappop(pq)

        for v, weight in adj[u]:
            if distance[v] > distance[u] + weight: #...If current distance is more than the distance of parent + parent to child, update it.
                distance[v] = distance[u] + weight
                hq.heappush(pq, (distance[v], v))  #....Pushing the new values of weight and node to heap.
    
    
    return distance

input_file = open("input/input01.txt", "r")
output_file = open("output/output01.txt", "w")

n , m = [int(i)+1 for i in input_file.readline().strip().split(" ")]

edges = []
for i in range(1, m):   #....The lab stask starts from 1
    edges.append([int(i) for i in input_file.readline().strip().split(" ")])

source = int(input_file.readline().strip())

adj = [[] for _ in range(n)]
for i in edges:
    adj[i[0]].append([i[1], i[2]])

result = djs(source, adj)

for i in range(1, n):
    if result[i] == float("inf"):
        print(-1, end=(" "), file=output_file)
    else:
        print(result[i], end=(" "), file=output_file)

output_file.close()      