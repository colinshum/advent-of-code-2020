from collections import defaultdict

def part_one(report, total):
  d = defaultdict(lambda: 0)

  for item in report:
    if d[total-item] > 0:
      return item * (total - item)
    else:
      d[item] += 1
  
  return 0

def part_two(report, total):
  d = defaultdict(lambda: 0)

  for item in report:
    result = part_one(report, total-item)
    if result != 0:
      return result * item

  return 0

if __name__ == "__main__":
  with open('./day1input.txt', 'r') as f:
      lines = f.readlines()
  i = [int(e.strip()) for e in lines]

  print(part_one(i, 2020))
  print(part_two(i, 2020))
