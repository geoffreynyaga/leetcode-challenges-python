class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)  # 1,2,
        value = (2 * (sum(set_nums))) - sum(nums)

        print(value, "value")

        return value

        # pairs = []
        # removed = []
        # correct =  []

        # for index_of_num in range((len(nums))):

        #     num = nums[index_of_num]

        #     if index_of_num == 0:
        #         removed.append(num)
        #         correct.append(num)
        #     else:
        #         if num in removed:
        #             pairs.append(num)
        #             if num in correct:
        #                 correct.remove(num)
        #         else:
        #             correct.append(num)

        #         removed.append(num)

        # return correct[0]


sol_instance = Solution()

x = sol_instance.singleNumber([2, 2, 1])

print(x, "x")


# return(2*sum(set(nums))-sum(nums))
