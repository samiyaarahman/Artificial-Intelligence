import heapq
graph = {
    'S': {'A': 5, 'B': 2, 'C': 4},
    'A': {'D': 9, 'E': 4},
    'B': {'G': 6},
    'C': {'F': 2},
    'D': {'H': 7},
    'E': {'G': 6},
    'F': {'G': 1},
    'G': {},   
    'H': {}    
}

def uniform_cost_search(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start])) 

    Attended= set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, cost

        if node in  Attended:
            Attended.add(node)
         

        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    return None, None



start = input("Enter Start Node: ").strip().upper()
goal = input("Enter Goal Node: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid node name! Check your inputs.")
else:
    path, total_cost = uniform_cost_search(start, goal)

    if path is None:
        print("\nNo path found from", start, "to", goal)
    else:
        print("\nShortest Path:", " → ".join(path))
        print("Total Path Cost:", total_cost)
