def adjacency_list_to_matrix(graph):
    num_nodes = len(graph)
    nodes = list(graph.keys())
    matrix = [[0] * num_nodes for _ in range(num_nodes)]

    for node in graph:
        for neighbour in graph[node]:
            i = nodes.index(node)
            j = nodes.index(neighbour)
            matrix[i][j] = 1

    for row in matrix:
        print(row)   

    return matrix

adjacency_list_to_matrix({0: [], 1: [], 2: []})
adjacency_list_to_matrix({0: [1], 1: [0]})
adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})
