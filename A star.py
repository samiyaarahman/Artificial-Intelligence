import heapq
import math

graph = {
    'S': {'A': 1, 'B': 5, 'C': 8},
    'A': {'D': 3, 'E': 7, 'G': 9},
    'B': {'G': 4},
    'C': {'G': 5},
    'D': {},
    'E': {},
    'G': {}
}

h = {
    'S': 8,
    'A': 8,
    'B': 4,
    'C': 3,
    'D': math.inf,
    'E': math.inf,
    'G': 0,   
    
}
def a_star(start, goal):
    pq = [(h[start], start, 0, [start])]
    Attended = set()
   

    while pq:   
        
        f, node, g_cost, path = heapq.heappop(pq)


        if node in Attended:
             continue   
        Attended.add(node)

 
        if node == goal:
            print("Number of Tested Node", Attended)
            return path, g_cost

        for neighbor in graph[node]:
            cost = graph[node][neighbor]
            g_new = g_cost + cost
            f_new = g_new + h[neighbor]

            heapq.heappush(pq, (f_new, neighbor, g_new, path + [neighbor]))

    return None, None


start = input("Enter Start Node: ").strip().upper()
goal = input("Enter Goal Node: ").strip().upper()

path, cost = a_star(start, goal)

if path:
    print("\nOptimal Path:", " → ".join(path))
    print("Total Path Cost:", cost)
else:
    print("No path found!")
