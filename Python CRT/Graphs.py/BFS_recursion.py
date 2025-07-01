def bfs_recursion(graph,node,visited):
    if node not in visited:
        print(node)
        visited.add(node)
        bfs_recursion(graph,node,visited)
graph={
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[],
}
visit=set()
bfs_recursion(graph,'A',visit)