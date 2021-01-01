
n = int(input())
count = 1
stack = []
result = []

for i in range(n) :
 stackNum = int(input())
 while count <= stackNum :
   stack.append(count)
   count += 1
   result.append("+")

 if stack[-1] == stackNum:
    stack.pop()
    result.append("-")
 else :
    print("NO")
    exit(0)

print('\n'.join(result))






