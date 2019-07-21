"""Que: Given an array of integers, find the highest product you can get from three of the integers.
If array size is less than 3, please printout -1.

* The range of integer is -1000 to 1000."""

input_array = input()
str_nums = input_array.split(',')

if len(str_nums) < 3:
  print(-1)

for i, num in enumerate(str_nums):
  num = int(str_nums[i])
  if num not in range(-1000, 1000):
    break
  if num < 0:
    num = -1 * num
  str_nums[i] = num

str_nums.sort(reverse=True)
print(str_nums[0] * str_nums[1] * str_nums[2])