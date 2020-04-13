"""Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # total_sum = sum(nums)
        # max_num = max(nums)

        # if len(nums) == 0:
        #     return "No number in array"
        # elif len(nums) == 1:
        #     return nums[0]
        # else:
        #     pass

        # # Input: [-2,1,-3,4,-1,2,1,-5,4],
        # final_values = []
        # current_value = 0

        # for index in range(len(nums)):
        #     print(index, "index ------1")
        #     sums = {}
        #     if nums[index] <= 0:
        #         pass
        #     else:
        #         current_value = nums[index]

        #         semi_global_index = index
        #         print(semi_global_index, "semi")

        #         counter = 0
        #         print(semi_global_index, "counter")

        #         for new_index in range(semi_global_index, len(nums) - 1):
        #             print(new_index - 1, "new_index ------2")
        #             new_index = new_index - 1
        #             x = nums[new_index + 1]

        #             # for fin_index in range(new_index, len(nums) - 1 ):

        #             new_sum = current_value + nums[new_index + 2]
        #             current_value = new_sum

        #             try:
        #                 if sums[nums[new_index]["sum"]] < new_sum:
        #                     sums.update(
        #                         {
        #                             nums[new_index]: {
        #                                 "sum": new_sum,
        #                                 "first_index": semi_global_index + counter,
        #                                 "last_index": new_index + 2,
        #                             }
        #                         }
        #                     )

        #             except:
        #                 sums[nums[new_index]] = {
        #                     "sum": new_sum,
        #                     "first_index": semi_global_index + counter,
        #                     "last_index": new_index + 2,
        #                 }

        #             counter += 1

        #         return sums

        #     final_values.append(sums)

        # return final_values

        # import math

        # if not nums:
        #     return 0
        # local_max1, global_max1 = 0, -math.inf
        # for i in range(len(nums)):
        #     local_max1 = max(local_max1 + nums[i], nums[i])
        #     global_max1 = max(global_max1, local_max1)

        # return global_max1

        length = len(nums)
        ps = [0] * length
        ps[0] = nums[0]
        for i in range(1, length):
            ps[i] = ps[i - 1] + nums[i]

        max_sum = ps[0]
        mini = 0
        for i in ps:
            max_sum = max(i - mini, max_sum)
            mini = min(i, mini)
        return max_sum

        # windowSum = nums[0]
        # maxSum = nums[0]

        # for i in range(1,len(nums)):
        #     windowSum = max(windowSum+nums[i], nums[i])
        #     maxSum = max(windowSum, maxSum)
        # return maxSum

        # js

        """let maxSubArray = function(nums) {
        let maxCurrent = nums[0];
        let maxGlobal = nums[0];

        for (let i = 1; i < nums.length ; i++) {
        maxCurrent = Math.max(nums[i], maxCurrent + nums[i]);
        if (maxCurrent > maxGlobal) {
            maxGlobal = maxCurrent;
        }
        }

        return maxGlobal;
         };"""


sol_instance = Solution()

x = sol_instance.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(x, "x")
print(type(x), "x")
