#!/usr/bin/env python
"""
Liar Liar Puzzle Solution

This puzzle is a bipartite graph problem. The key insight is that if person A
accuses person B, they must be in different groups (honest vs liar):
- If A is honest and accuses B, then B is a liar
- If A is a liar and accuses B, then B is honest (liars lie)

Algorithm: Use BFS to 2-color the graph where nodes are people and edges are accusations.
Time Complexity: O(V + E) where V = number of members, E = number of accusations
Space Complexity: O(V + E)
"""

import sys
from collections import defaultdict, deque


def solve_liar_liar(filename):
    """
    Solve the Liar Liar puzzle using bipartite graph coloring.

    Args:
        filename: Path to input file

    Returns:
        Tuple of (larger_group_size, smaller_group_size)
    """
    # Build adjacency list from input
    graph = defaultdict(list)
    members = set()

    with open(filename, 'r') as f:
        n = int(f.readline().strip())

        for _ in range(n):
            line = f.readline().strip().split()
            accuser = line[0]
            m = int(line[1])

            members.add(accuser)

            for _ in range(m):
                accused = f.readline().strip()
                members.add(accused)
                # Add bidirectional edge (accusation creates a constraint)
                graph[accuser].append(accused)
                graph[accused].append(accuser)

    # 2-color the graph using BFS (bipartite partitioning)
    color = {}

    for start_member in members:
        if start_member in color:
            continue

        # BFS from this unvisited component
        queue = deque([start_member])
        color[start_member] = 0

        while queue:
            person = queue.popleft()
            current_color = color[person]
            next_color = 1 - current_color

            for neighbor in graph[person]:
                if neighbor in color:
                    # Verify graph is bipartite (shouldn't fail per problem statement)
                    if color[neighbor] != next_color:
                        raise ValueError("Graph is not bipartite - no valid solution")
                else:
                    color[neighbor] = next_color
                    queue.append(neighbor)

    # Count members in each group
    group0 = sum(1 for c in color.values() if c == 0)
    group1 = len(color) - group0

    # Return larger group first, then smaller group
    return max(group0, group1), min(group0, group1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python liar_liar.py <input_file>", file=sys.stderr)
        sys.exit(1)

    larger, smaller = solve_liar_liar(sys.argv[1])
    print(f"{larger} {smaller}")
