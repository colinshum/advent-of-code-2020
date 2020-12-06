def p1(report, total)
  d = {}

  report.each { |item| d.dig(item) ? (return item * (total - item)) : d[total - item] = 1 }

  return 0
end

def p2(report, total)
  d = {}

  report.each do |item|
    result = p1(report, total - item)
    return result * item if result != 0
  end

  return 0
end

if __FILE__ == $0
  data = []
  File.foreach("day1/day1input.txt") { |line| data << line.chomp.to_i }
  puts p1(data, 2020)
  puts p2(data, 2020)
end
