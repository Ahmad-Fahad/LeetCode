# nums[] , target
target = 9
nums = [2, 7, 11, 15]
#.......
hash_map = {}
for i in range(len(nums)):
    hash_map[nums[i]] = i
for i in range(len(nums)):
    c = target - nums[i]
    if c in hash_map and hash_map[c] != i:
        print(i, hash_map[c])
        break # for local testing
        


"""

target = 9
nums = [2, 7, 11, 15]
print(nums)
hash_map = {}
for i in range(len(nums)):
    hash_map[nums[i]] = i
print(hash_map)
for i in range(len(nums)):
    c = target-nums[i]
    if c in hash_map and hash_map[c] != i:
        print(i, hash_map[c])
        break






lst = [int(x) for x in input().split()]
target = int(input())
limit = len(lst)
for i in range(limit):
    for j in range(i+1, limit):
            sum = lst[i] + lst[j]
            if(sum == target):
                print(f"[{i},{j}]")
                break
"""