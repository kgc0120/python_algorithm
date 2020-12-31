# baekjoon
# 2920 음계 

num = list(map(int, input().split()))

arr = sorted(num)
re_arr = reversed(arr)
if num == arr :
  print("ascending")
elif num == list(re_arr):
  print("descending")
else :
  print("mixed")