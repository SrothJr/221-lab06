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

#...Structure of the code starts from here!
input_file = open("input/input02.txt", "r")
output_file = open("output/output02.txt", "w")

n , m = [int(i)+1 for i in input_file.readline().strip().split(" ")]

edges = []
for i in range(1, m):   #....The lab stask starts from 1
    edges.append([int(i) for i in input_file.readline().strip().split(" ")])

alice , bob = [int(i) for i in input_file.readline().strip().split(" ")]

adj = [[] for _ in range(n)]
for i in edges:
    adj[i[0]].append([i[1], i[2]])

#....Commented out prints for debugging

# print(n, m)
# print(alice, bob)
# print(edges)
# print()
# print(adj)
# print()

alice_dist = djs(alice, adj)
bob_dist = djs(bob, adj)

# print(alice_dist, bob_dist)

min_time = float("inf")
node = -1
for i in range(n):
    if alice_dist[i] != float("inf") and bob_dist[i] != float("inf"):
        if alice_dist[i] >= bob_dist[i]:
           time_taken = alice_dist[i]
        else:
            time_taken = bob_dist[i]
        if time_taken < min_time:
            min_time = time_taken
            node = i


if min_time == float("inf") or node == -1:
    print("Impossible", file= output_file)
else:
    print("Time: ", min_time, file= output_file)
    print("Node: ", node, file= output_file)

output_file.close()