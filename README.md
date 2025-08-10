# Python-directed-graph-bfs

Check if two nodes are connected in a directed graph using **Breadth-First Search (BFS)**.

## Overview
This project implements:
- A directed graph data structure
- Supporting data structures (linked list, priority queue, stack)
- BFS-based connectivity check
- File parsing for graph data
- Automated tests for file handling

## File descriptions
- **DirectedGraph.py** – Directed graph representation (nodes, edges, neighbours)
- **DirectedList.py** / **OneCell.py** – Lightweight linked list implementation
- **Edge.py** – Edge class for graph connections
- **PrioQueueDirectedList.py** – Priority queue built on DirectedList
- **Stack1Cell.py** – Stack (LIFO) structure *(note: not suitable for BFS)*
- **isConnected.py** – Main program; loads a graph from file and runs BFS to check connectivity
- **test_file_handling.py** – Tests for file parsing and error handling
- **map1.map / map2.map / airmap1.map** – Example graph files
- **Exempelgraf.jpg** – Example graph illustration

## How to run
1. Ensure Python 3 is installed.
2. From the project directory, run:
```bash
python3 isConnected.py
```
3. At the prompt, type:
```
A B
```
to check if there is a path from node `A` to node `B`.

Type `quit` to exit.

## Running tests
To run the tests:
```bash
python3 -m pytest -q
```

## License
This project is for personal, educational, and demonstration purposes only.  
See the LICENSE file for details.
