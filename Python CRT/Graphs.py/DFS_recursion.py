def dfs_recursion(graph,node,visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs_recursion(graph,neighbour,visited)
graph={
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[],
}
visit=set()
dfs_recursion(graph,'A',visit)