li = []

f = open("day_2_data.txt", "r")

for line in f:
  li.append(line.rstrip())


def is_valid(line):
  params, letter, pw = line.split()
  letter = letter.replace(":", "")
  minimum, maximum = params.split("-")

  return int(minimum) <= pw.count(letter) <= int(maximum)

def is_valid_2(line):
  params, letter, pw = line.split()
  letter = letter.replace(":", "")
  pos_1, pos_2 = params.split("-")
  pos_1 = int(pos_1)
  pos_2 = int(pos_2)
  return (pw[int(pos_1)-1] == letter) ^ (pw[int(pos_2)-1] == letter)

def valid_count(li, func):
  count = 0
  for line in li:
    if(func(line)):
      count+=1
  return print(count)

valid_count(li, is_valid)
valid_count(li, is_valid_2)