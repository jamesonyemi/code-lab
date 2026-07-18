"""
A template for Breadth-First-Search for Trees Data Structure

Used this pattern when you're:
 1. traversing a tree from 'top to bottom'
 2. or root to leaves nodes
 3. when you care about depth, distance, level-based logic
 4. looking for the first match/closest node to the root

  Tip: Tree breadth-first-search, is always from left to right
"""

from collections import deque

def tree_bfs(root):
	queue = deque([root])
	while len(queue) > 0:
		node = queue.popleft()
		for child in node.children:
			if is_goal(child):
				return FOUND(child)
		queue.append(child)	
	
	return NOT_FOUND	

