
"""
Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000
"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0

        current_count = 0

        results= {}

        # d = {}

        # maxlen,count = 0, 0

        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         count -= 1

        #     if count == 0:
        #         maxlen = i + 1
        #     if count in d:
        #         maxlen = max(maxlen,i-d[count])
        #     else:
        #         d[count] = i

        # return maxlen



        for index in range(len(nums)):

            if nums[index] == 0:
                current_count -= 1
            else:
                current_count += 1

            if  current_count in results:
                # results[current_count] = (index - results[current_count])
                # print(max_length,((index - results[current_count]) + 1),"comparison")
                max_length = max(max_length, ((index - results[current_count])))
            elif current_count == 0:
                # results[current_count] = index
                max_length = max(max_length, (index + 1))
            else:
                results[current_count] = index

        print(results, "results")
        print(max_length, "max length")

        return max_length

        """
        Runtime: 772 ms, faster than 91.47% of Python online submissions for Contiguous Array.
        Memory Usage: 17.5 MB, less than 50.00% of Python online submissions for Contiguous Array.
        """


        # for item in results:
        #     print(item[0],"item")


            # if index != 0:
            #     if nums[index] != last_num:
            #         current_count += 1
            #         if (current_count % 2) == 0:
            #             max_length = max(current_count, max_length)
            #     else:
            #         current_count = 0

            #     last_num = nums[index]
            # else:
            #     last_num = nums[index]
            #     current_count += 1
            # print(max_length)
            # current_count = 0

            # for index2 in range(index,len(nums)):
            #     if nums[index2] == 0:
            #         current_count -= 1
            #     else:
            #         current_count += 1

            #     if current_count == 0:
            #         # max_length = max(current_count, max_length)
            #         max_length = max(max_length,((index2-index)+1))
            #         # first_index = index2

        # return max_length



sol_instance = Solution()

x = sol_instance.findMaxLength([0,1,0,1])
print(x,"x")
