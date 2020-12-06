def password(i):
  count = 0

  for line in lines:
    temp = line.split()
    minmax = temp[0].split('-')
    minimum = int(minmax[0])
    maximum = int(minmax[1])
    letter = temp[1][0]
    password = temp[2]

    # print("min: " + minmax[0] + " max: " + minmax[1] + " letter: " + temp[1][0] + " password: " + temp[2])

    if minimum <= password.count(letter) <= maximum:
      count += 1

  return count

def password_two(i):
  count = 0

  for line in lines:
    temp = line.split()
    minmax = temp[0].split('-')
    i1 = int(minmax[0]) - 1
    i2 = int(minmax[1]) - 1
    letter = temp[1][0]
    password = temp[2]

    if (password[i1] == letter or password[i2] == letter) and password[i1] != password[i2]:
      count += 1
    
  return count


  
if __name__ == "__main__":
  with open('day2/day2input.txt', 'r') as f:
    lines = f.readlines()

  print(password(lines))
  print(password_two(lines))

    # print(line)
