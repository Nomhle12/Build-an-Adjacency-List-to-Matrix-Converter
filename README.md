# Build-an-Adjacency-List-to-Matrix-Converter
A Python implementation that converts an unweighted graph represented as an adjacency list into an adjacency matrix.

## Description

Graphs can be represented in several different ways. This project demonstrates how to convert an adjacency list into an adjacency matrix using Python.The function accepts a dictionary representing an unweighted graph. Each dictionary key represents a node, while the corresponding list contains the nodes connected to it.

The function then:
1. Determines the number of nodes in the graph.
2. Creates an empty adjacency matrix filled with 0s.
3. Identifies the position of each node in the matrix.
4. Sets matrix values to 1 when an edge exists.
5. Prints each row of the resulting matrix.
6. Returns the completed adjacency matrix.

## Example
Test Case 1: Three disconnected nodes
adjacency_list_to_matrix({0: [], 1: [], 2: []})

Output:
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]

Test Case 2: Two connected nodes
adjacency_list_to_matrix({0: [1], 1: [0]})

Output:
[0, 1]
[1, 0]

Test Case 3: Multiple connected nodes
adjacency_list_to_matrix({
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
})

Output:
[0, 1, 1, 0]
[0, 0, 1, 0]
[1, 0, 0, 1]
[0, 0, 1, 0]

## Concepts Demonstrated
*Graph representation
*Adjacency lists
*Adjacency matrices
*Dictionaries
*Lists
*Nested loops
*List indexing
*Matrix creation
*Basic graph algorithms
