# Liar Liar Puzzle Solution

## Problem Summary

Given a discussion board where each member is either always honest or always a liar, and each member provides accusations about who is lying, determine the sizes of the two groups (honest vs liars).

## Algorithm: Bipartite Graph 2-Coloring

### Key Insight

When person A accuses person B of being a liar:
- **If A is honest** → B must be a liar (honest people tell the truth)
- **If A is a liar** → B must be honest (liars always lie)

Therefore, **any two people connected by an accusation must be in different groups**.

This transforms the problem into a **bipartite graph partitioning** problem.

### Graph Representation

- **Nodes**: Each member is a node
- **Edges**: Each accusation creates an undirected edge between accuser and accused
- **Goal**: 2-color the graph such that adjacent nodes have different colors

### Algorithm Steps

1. **Parse Input**: Build an adjacency list from accusations
2. **BFS 2-Coloring**:
   - For each connected component, use BFS to assign colors (0 or 1)
   - Adjacent nodes get opposite colors
   - Handle disconnected components by starting BFS from unvisited nodes
3. **Count Groups**: Count nodes with each color
4. **Output**: Return counts in descending order (larger group, smaller group)

### Complexity Analysis

- **Time Complexity**: O(V + E)
  - V = number of members
  - E = number of accusations
  - BFS visits each node and edge once

- **Space Complexity**: O(V + E)
  - Adjacency list storage: O(E)
  - Color mapping: O(V)
  - BFS queue: O(V) worst case

### Why This Is Optimal

1. **Linear Time**: O(V + E) is optimal since we must read all input
2. **Single Pass**: BFS visits each node exactly once
3. **Minimal Space**: Only stores necessary graph structure
4. **Handles All Cases**: Works for disconnected graphs and any valid bipartite graph

## Usage

```bash
python liar_liar.py <input_file>
```

## Example

**Input (test_input.txt):**
```
5
Stephen   1
Tommaso
Tommaso   1
Galileo
Isaac     1
Tommaso
Galileo   1
Tommaso
George    2
Isaac
Stephen
```

**Output:**
```
3 2
```

**Explanation:**
- Group 1 (Honest): Stephen, Galileo, Isaac (3 members)
- Group 2 (Liars): Tommaso, George (2 members)

The graph structure:
```
Stephen -- Tommaso -- Galileo
   |          |
 George     Isaac
   |
  Isaac
```

All edges connect members from different groups, confirming a valid bipartite partition.
