from typing import List

from flood_fill import flood_fill as _shared_flood_fill


def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    return _shared_flood_fill(r, c, replacement, image)


if __name__ == "__main__":
    sample = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(flood_fill(1, 1, 2, sample))