"""
A template for graph Breadth-First-Search

Used this pattern when:
 1. working with grids, adjascency lists or network
 2. the structure can contain cycles or duplicate paths
 3. Need to find the shortest number of steps or minimum moves
 4. Exploring possible states
"""

def graph_bfs(root):
	queue   = deque([root])
	visited = set([root])
	while len(queue) > 0:
		node = queue.popleft()
		for neighbor in get_neighbor(node):
			if neighbor in visited:
				continue
			queue.append(neighbor)
			visited.add(neighbor)
