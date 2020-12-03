li = []

f = open("day_1_data.txt", "r")

for line in f:
  for num in line.split():
    li.append(int(num))

def find_sum_2(li, target=2020):
  for i in li:
    j = target - i
    if j in li:
      return print(i * j)

def find_sum_3(li, target=2020):
  for i in li:
    for j in li:
      if i + j < target and i != j:
        for k in li:
          if k != i and k != j:
            if i+j+k == target:
              return print(i*j*k)

find_sum_2(li)
find_sum_3(li)