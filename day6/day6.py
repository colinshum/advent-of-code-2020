def p1(li):
  ml = 0

  for x in li:
    a = x.split(" ")
    b = set(''.join(set(a)))
    ml += len(b)

  return ml


def p2(li):
  ml = 0

  for x in li:
    a = x.split(" ")
    b = [set(i) for i in a]
    c = set.intersection(*b)
    ml += len(c)

  return ml


if __name__ == "__main__":
  with open('day6/day6input.txt', 'r') as f:
    lines = f.read()
  li = [i.replace("\n", " ").strip() for i in lines.split("\n\n")]

  print(p1(li))
  print(p2(li))
