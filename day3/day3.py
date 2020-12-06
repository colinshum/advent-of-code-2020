def tobaggan(i, right, down):
  x_max, y_max = len(i[0]), len(i)
  x, y, count = 0, 0, 0

  while y < y_max:
    if i[y][x%x_max] == '#':
      count += 1
    
    x += right
    y += down
  
  return count

def tobaggan_product(i, paths):
  # paths: listOf(listOf(Int))
  # example: [[r1, d1], [r2, d2], [r3, d3]] 
  result = 1

  for path in paths:
    result *= tobaggan(i, path[0], path[1])

  return result

if __name__ == "__main__":
  with open('day3/day3input.txt', 'r') as f:
    lines = f.readlines()
  
  i = [i.strip() for i in lines]

  print(tobaggan(i, 1, 3))
  print(tobaggan_product(i, [[1,1], [3,1], [5,1], [7,1], [1,2]]))
