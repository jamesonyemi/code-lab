from collections import deque
from typing import List, Tuple


def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
	if not image or not image[0]:
		return image

	num_rows, num_cols = len(image), len(image[0])
	if not (0 <= r < num_rows and 0 <= c < num_cols):
		return image

	original_color = image[r][c]
	if original_color == replacement:
		return image

	def get_neighbors(coord: Tuple[int, int], color: int):
		row, col = coord
		deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
		for dr, dc in deltas:
			nr, nc = row + dr, col + dc
			if 0 <= nr < num_rows and 0 <= nc < num_cols and image[nr][nc] == color:
				yield nr, nc

	def bfs(start: Tuple[int, int]):
		queue = deque([start])
		visited = [[False] * num_cols for _ in range(num_rows)]
		sr, sc = start
		visited[sr][sc] = True
		image[sr][sc] = replacement

		while queue:
			node = queue.popleft()
			for nbr in get_neighbors(node, original_color):
				nr, nc = nbr
				if visited[nr][nc]:
					continue
				visited[nr][nc] = True
				image[nr][nc] = replacement
				queue.append((nr, nc))

	bfs((r, c))
	return image

