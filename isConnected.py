# -*- coding: utf-8 -*-
# Written by [Your Name] <your.email@umu.se>
# Usage except those listed above requires permission by the author.
"""
Main program that loads a directed graph from file and checks if a path exists
between two nodes using breadth-first search (BFS).
"""

import sys
from DirectedGraph import DirectedGraph
from Edge import Edge
from Stack1Cell import Stack1Cell  # Used as a queue

def loadGraph(filename):
    """
    Purpose: Load a directed graph from file.
    Parameters: filename - name of the file (string)
    Returns: DirectedGraph object
    Raises: ValueError or exits if the file is invalid or not found
    """
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    graph = DirectedGraph(lambda a, b: a == b)
    edgeCount = None

    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        parts = line.split()

        if edgeCount is None:
            try:
                edgeCount = int(parts[0])
            except:
                print("Bad file format")
                sys.exit(1)
            continue

        if len(parts) < 2:
            print("Bad file format")
            sys.exit(1)

        node1 = parts[0]
        node2 = parts[1]

        for n in [node1, node2]:
            if not any(graph._eqFcn(n, v._vertice) for v in graph._nodes):
                graph.insertNode(n)
        graph.insertEdge(Edge(node1, node2))

    return graph

def bfs(graph, start, target):
    """
    Purpose: Check if a path exists from start to target using BFS.
    Parameters: graph - DirectedGraph object
                start - starting node name (string)
                target - target node name (string)
    Returns: True if path exists, False otherwise
    """
    visited = []
    queue = Stack1Cell()
    queue.push(start)
    visited.append(start)

    while not queue.isempty():
        current = queue.top()
        queue.pop()
        if graph._eqFcn(current, target):
            return True
        for neighbor in graph.neighbours(current):
            if neighbor not in visited:
                visited.append(neighbor)
                queue.push(neighbor)
    return False

def main():
    """
    Purpose: Main loop that reads input and performs connectivity queries.
    """
    if len(sys.argv) != 2:
        print("Usage: python isConnected.py <filename>")
        sys.exit(1)

    graph = loadGraph(sys.argv[1])

    while True:
        print("Enter origin and destination (quit to exit):", end=" ")
        line = input().strip()
        if line == "quit":
            break
        parts = line.split()
        if len(parts) != 2:
            print("Invalid input")
            continue
        start, end = parts[0], parts[1]
        if start == end:
            print(f"{start} and {end} are connected")
        elif bfs(graph, start, end):
            print(f"{start} and {end} are connected")
        else:
            print(f"{start} and {end} are not connected")

if __name__ == "__main__":
    main()
