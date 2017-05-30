from math import *

NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH} # old -> new direction

def spiral(width, height):
  if width < 1 or height < 1:
    raise ValueError
  x, y = width // 2, height // 2 # start near the center
  dx, dy = NORTH # initial direction
  matrix = [[None] * width for _ in range(height)]
  count = 0
  while True:
    count += 1
    matrix[y][x] = count
    new_dx, new_dy = turn_right[dx,dy]
    new_x, new_y = x + new_dx, y + new_dy
    if (0 <= new_x < width and 0 <= new_y < height and
      matrix[new_y][new_x] is None):
      x, y = new_x, new_y
      dx, dy = new_dx, new_dy
    else:
      x, y = x + dx, y + dy
      if not (0 <= x < width and 0 <= y < height):
        return matrix

def main():
  size = 1001
  spi = spiral(size,size)
  result = 0
  for i in range(size):
    result += spi[i][i]
  for i in range(size):
    result += spi[size-1-i][i]
  result -= spi[int(size/2)][int(size/2)]

  print result


main()