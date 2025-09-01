graph  {
    1:[2,3],
    2:[4,5],
    3:[],
    4:[],
    5:[]
}

visited = set()
stack = [1]

while stack:
    node = stack.pop
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        stack.extend(reversed(graph[node]))
