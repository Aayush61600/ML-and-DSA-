# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Approach 1: Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range (i+1, len(nums)):
                if (nums[i]+ nums[j] == target):
                    return [i,j]
                
        return [] 
    

# Approach 2: Hash Table    