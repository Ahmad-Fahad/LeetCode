class Solution:
	def thirdMax(self, nums: List[int]) -> int:
		max_1 = max_2 = max_3 = None
		for i in nums:
			if (i == max_1) or (i == max_2) or (i == max_2):
				continue 
			else:
				if max_1 is None:
					max_1 = i
				elif i > max_1: 
					max_3 = max_2
					max_2 = max_1
					max_1 = i
				elif max_2 is None:
					max_2 = i
				elif i > max_2: 
					max_3 = max_2
					max_2 = i
				elif (max_3 is None) or  (i > max_3): 
					max_3 = i
				 
		if max_3 is None:
			return max_1
		else:
			return max_3
 	

 

lst = [3, 1]
print(lst, thirdMax(lst))

lst = [2, 2, 3, 1]
print(lst, thirdMax(lst))

lst = [2, 1]
print(lst, thirdMax(lst))

lst = [ 2, 3, 1]
print(lst, thirdMax(lst))
