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

def dfs(start, goal):
    stack= [(start, [start], 0)]  
    Attended= set()
    Tested_node=0

    while stack:
        node, path, cost = stack.pop()
        Tested_node+=1

        if node == goal:
            print("Total Tested Nodes:", Tested_node) 
            return path, cost

        if node not in Attended:
            Attended.add(node)

      
        for neighbor, edge_cost in reversed(list(graph[node].items())):
            if neighbor not in Attended:
                stack.append((neighbor, path + [neighbor], cost + edge_cost))
               

    return None, None

start = input("Enter Start Node: ").strip().upper()
goal = input("Enter Goal Node: ").strip().upper()

if start not in graph or goal not in graph:
    print("Invalid node name! Check your inputs.")
else:
    path, total_cost = dfs(start, goal)

    if path is None:
        print("\nNo path found from", start, "to", goal)
    else:
        print("\nDFS Path:", " → ".join(path))
        print("Total Path Cost:", total_cost)
       
     
