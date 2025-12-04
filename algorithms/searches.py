def dfs(graph: dict, currentNode: str, visited: list):
    visited.append(currentNode)
    for node in graph[currentNode]:
        if node not in visited:
            dfs(graph, node, visited)
        
    return visited

def bfs(graph: dict, startNode: str):
    queue = []
    visited = []
    queue.append(startNode)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
    return visited

graph = {
         "A":["B","D","E"],
         "B":["A","C","D"],
         "C":["B","G"],
         "D":["A","B","E","F"],
         "E":["A","D"],
         "F":["D"], 
         "G":["C"]
        }


print(dfs(graph,"A",[]))
print(bfs(graph, "A"))