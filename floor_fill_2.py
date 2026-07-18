from collections import deque
from typing import List

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    if not image or not image[0]:
        return image

    num_rows = len(image)
    num_cols = len(image[0])
    if not (0 <= r < num_rows and 0 <= c < num_cols):
        return image

    original_color = image[r][c]
    if original_color == replacement:
        return image

    queue = deque([(r, c)])
    image[r][c] = replacement

    while queue:
        row, col = queue.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if 0 <= nr < num_rows and 0 <= nc < num_cols and image[nr][nc] == original_color:
                image[nr][nc] = replacement
                queue.append((nr, nc))

    return image


if __name__ == "__main__":
    sample = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(flood_fill(1, 1, 2, sample))