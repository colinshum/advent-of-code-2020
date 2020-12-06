def p1(i)
  c = 0

  i.each { |h| c += 1 if h[:minmax][0].to_i <= h[:password].count(h[:letter]) and h[:password].count(h[:letter]) <= h[:minmax][1].to_i }

  return c
end

def p2(i)
  c = 0

  i.each do |h|
    pw = h[:password]
    l = h[:letter]
    i1 = h[:minmax][0]
    i2 = h[:minmax][1]

    c += 1 if (pw[i1] == l or pw[i2] == l) and pw[i1] != pw[i2]
    
  end

  return c
end

if __FILE__ == $0
  data = []
  parsed = []
  File.foreach("day2/day2input.txt") { |line| data << line.chomp }
  
  data.each do |i|
    temp = i.split(" ")
    parsed << { 'minmax': temp[0].split('-'), 'letter': temp[1][0], 'password': temp[2] }
  end

  # puts parsed.to_s
  puts p1(parsed)
  puts p2(parsed)
end
