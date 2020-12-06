import re

def passport(i, fields):
  count = 0

  for x in li:
    temp_list = x.strip().split(" ")
    d = {}

    for y in temp_list:
      kv = y.split(":")
      d[kv[0]] = kv[1]

    if required.issubset(set(d.keys())):
      count += 1
    
  return count

def validate_passport(d):
  # check bad birth years
  if not (1920 <= int(d['byr']) <= 2002 and len(d['byr']) == 4):
    # print("Failed byr: " + d['byr'])
    # print(d)
    # print()
    return False

  if not (2010 <= int(d['iyr']) <= 2020 and len(d['iyr']) == 4):
    # print("Failed iyr: " + d['iyr'])
    # print(d)
    # print()
    return False
  
  if not (2020 <= int(d['eyr']) <= 2030 and len(d['eyr']) == 4):
    # print("Failed eyr: " + d['eyr'])
    # print(d)
    # print()
    return False

  if ((d['hgt'][-2:] == "cm" and not 150 <= int(d['hgt'][:-2]) <= 193) or (d['hgt'][-2:] == "in" and not 59 <= int(d['hgt'][:-2]) <= 76)):
    # print("Failed hgt: " + d['hgt'])
    # print(d)
    # print()
    return False

  nl = re.compile('[^a-f0-9]').search
  if bool(nl(d['hcl'][1:])) or d['hcl'][0] != "#" or len(d['hcl']) != 7:
    # print("Failed hcl: " + d['hcl'])
    # print(d)
    # print()
    return False

  ecl = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

  if not (d['ecl'] in ecl):
    # print("Failed ecl: " + d['ecl'])
    # print(d)
    # print()
    return False

  if len(d['pid']) != 9:
    # print("Failed pid: " + d['pid'])
    # print(d)
    # print()
    return False

  return True

def passport_two(i, fields):
  count = 0

  for x in li:
    temp_list = x.strip().split(" ")
    d = {}

    for y in temp_list:
      kv = y.split(":")
      d[kv[0]] = kv[1]

    if required.issubset(set(d.keys())):
      if validate_passport(d):
        count += 1
    
  return count - 1

if __name__ == "__main__":
  with open('day4/day4input.txt', 'r') as f:
    lines = f.read()
  li = [i.replace("\n", " ") for i in lines.split("\n\n")]

  required = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
  
  print(passport(li, required))
  print(passport_two(li, required))
