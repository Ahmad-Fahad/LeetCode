nums = [1,1,2,2,3,4,4, 5,5,5,5, 6]
n = len(nums)
current_index = 1
for i in range(1, n):
	if nums[i] != nums[i-1]:
		nums[current_index] = nums[i]
		current_index += 1
	else:
		continue
#return current_index 
print(current_index)
for i in range(current_index):
	print(nums[i], end=" ")

'''
	submitted code :


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        current_index = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[current_index] = nums[i]
                current_index += 1
            else:
                continue
        return current_index 