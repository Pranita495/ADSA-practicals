def prim(graph):
    n = len(graph)
    selected = [False] * n
    selected[0] = True

    edges = []
    total_cost = 0

    for _ in range(n - 1):
        min_weight = float('inf')
        x = y = -1

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            x, y = i, j

        selected[y] = True
        edges.append((x, y, min_weight))
        total_cost += min_weight

    print("Edges in Minimum Spanning Tree:")
    for x, y, weight in edges:
        print(f"{x} - {y} : {weight}")

    print("Total cost:", total_cost)


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(graph)
