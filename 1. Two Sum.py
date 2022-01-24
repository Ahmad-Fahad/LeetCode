
flag=0
lst = [int(x) for x in input().split()]
target = int(input())
limit = len(lst)
for i in range(limit):
    for j in range(i+1, limit):
            sum = lst[i] + lst[j]
            if(sum == target):
                print(f"[{i},{j}]")
                break
  