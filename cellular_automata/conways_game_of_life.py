"""Conway's Game of Life implemented in Python.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life"""

from __future__ import annotations

from PIL import Image

GLIDER = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

BLINKER = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]

def new_generation(cells: list[list[int]]) -> list[list[int]]:
    """Generates the next generation for a given state of Conway's Game of Life."""
    next_gen = [[0] * len(row) for row in cells]
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            neighbours = sum(
                cells[x][y] for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
                if 0 <= x < len(cells) and 0 <= y < len(row) and (x != i or y != j)
            )
            next_gen[i][j] = 1 if cell == 1 and 2 <= neighbours <= 3 or cell == 0 and neighbours == 3 else 0
    return next_gen

def generate_images(cells: list[list[int]], frames: int) -> list[Image.Image]:
    """Generates a list of images of subsequent Game of Life states."""
    images = []
    for _ in range(frames):
        img = Image.new("RGB", (len(cells[0]), len(cells)))
        pixels = img.load()
        for x, row in enumerate(cells):
            for y, cell in enumerate(row):
                colour = 255 - cell * 255
                pixels[y, x] = (colour, colour, colour)
        images.append(img)
        cells = new_generation(cells)
    return images

if __name__ == "__main__":
    images = generate_images(GLIDER, 16)
    images[0].save("out.gif", save_all=True, append_images=images[1:])
