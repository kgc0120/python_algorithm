# baekjoon
# 2798 블랙잭

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
for i in range(N) :
  for j in range(i+1, N) :
    for k in range(j+1,  N) :
      sum = lst[i] + lst[j] + lst[k]
      if M >= sum :
        result = max(sum, result)

print(result)





