"""Given an array nums, wriall 0's to tte a function to move he end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations."""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for num in nums:
        #     if num == 0:
        #         nums.remove(num)
        #         nums.append(0)
        # return nums


        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i = i + 1

        # Fastest Solution
        j = 0 # position of 1st 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1



sol_instance = Solution()

x = sol_instance.moveZeroes([0,1,0,3,12])
print(x, "x")
