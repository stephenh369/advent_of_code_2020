arr = []

f = open("day_1_data.txt", "r")

for line in f:
  for num in line.split():
    arr.append(int(num))

def find_sum_2(arr, target=2020):
  for i in arr:
    j = target - i
    if j in arr:
      return print(i * j)

def find_sum_3(arr, target=2020):
  for i in arr:
    for j in arr:
      if i + j < target and i != j:
        for k in arr:
          if k != i and k != j:
            if i+j+k == target:
              return print(i*j*k)

find_sum_2(arr)
find_sum_3(arr)