RED_PINK = [[255, 0, i] for i in range(256)]
PINK_BLUE = [[i, 0, 255] for i in reversed(range(256))]
BLUE_AQUA = [[0, i, 255] for i in range(256)]
AQUA_GREEN = [[0, 255, i] for i in reversed(range(256))]
GREEN_YELLOW = [[i, 255, 0] for i in range(256)]
YELLOW_RED = [[255, i, 0] for i in reversed(range(256))]

RGB = RED_PINK + PINK_BLUE + BLUE_AQUA + AQUA_GREEN + GREEN_YELLOW + YELLOW_RED