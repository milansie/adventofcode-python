import numpy as np

def render_map(map_array: np.ndarray):
    print('\n'.join(''.join(np.where(row, '#', '.')) for row in map_array))


def init_map(width: int, height: int) -> np.ndarray:
    return np.zeros((height, width), dtype=bool)