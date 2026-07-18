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


def FOUND(node):
	"""Return a documented success payload for a matching node."""
	return ("FOUND", node)


NOT_FOUND = ("NOT_FOUND", None)


def tree_bfs(root, is_goal=None):
	"""Traverse the tree breadth-first and return FOUND(node) for the first matching node."""
	if is_goal is None:
		is_goal = lambda node: False

	if is_goal(root):
		return FOUND(root)

	queue = deque([root])
	while len(queue) > 0:
		node = queue.popleft()
		for child in node.children:
			if is_goal(child):
				return FOUND(child)
			queue.append(child)

	return NOT_FOUND