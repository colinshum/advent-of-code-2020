import math

def binary_search(s):
  row_low, row_hi = 0, 127
  col_low, col_hi = 0, 7

  for char in s[:7]:
    if char == 'F':
      row_hi = math.floor((row_hi - row_low) / 2 + row_low)
    else:
      row_low = math.ceil(row_hi - (row_hi - row_low) / 2)

  for char in s[7:10]:
    if char == 'R':
      col_low = math.ceil(col_hi - (col_hi - col_low) / 2)
    else:
      col_hi = math.floor((col_hi - col_low) / 2 + col_low) 

  return (row_low, col_low)

def binary(i):
  max_seat = 0

  for x in i:
    result = binary_search(x)
    rc = result[0] * 8 + result[1]
    
    if max_seat < rc:
      max_seat = rc

    
  return max_seat

def binary_two(i):
  r, c = 128, 8
  seats = [[0] * c for _ in range(r)]

  for x in i:
    result = binary_search(x) 
    seats[result[0]][result[1]] = 1

  for row in range(len(seats)):
    for col in range(len(seats[0])):
      if 1 < col < 6 and 1 < row < 126 and seats[row][col-1] == 1 and seats[row][col+1] == 1 and seats[row][col] == 0:
        return row * 8 + col

if __name__ == "__main__":
  with open('day5/day5input.txt', 'r') as f:
    lines = f.readlines()
  
  i = [i.strip() for i in lines]
  print(binary(i))
  print(binary_two(i))
