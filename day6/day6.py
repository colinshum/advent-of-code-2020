def p1(li):
  return sum([len(set(''.join(set(x.split(" "))))) for x in li])

def p2(li):
  return sum([len(set.intersection(*[set(i) for i in x.split(" ")])) for x in li])


if __name__ == "__main__":
  with open('day6/day6input.txt', 'r') as f:
    lines = f.read()
  li = [i.replace("\n", " ").strip() for i in lines.split("\n\n")]

  print(p1(li))
  print(p2(li))
