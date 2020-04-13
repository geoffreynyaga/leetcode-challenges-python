
from collections import Counter
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums =     [1, 1, 2, 2, 3, 6, 6, 9, 9]
        # set_nums = [1, 2, 3, 6, 9]

        refactored_dict = {}

        for index in range(len(nums)):
            try:
                refactored_dict[nums[index]] += 1
            except:
                refactored_dict[nums[index]] = 1

            # {
            #     "1": 3,
            #     "2": 5,
            # }

        set_nums = set(nums)

        fin_list = []

        for num in set_nums:
            if refactored_dict[num] == 1 and len(fin_list) <= 2:
                fin_list.append(num)

        return fin_list

        # c = Counter(nums)
        # fin_list = []

        # for num in nums:
        #     if c[num] == 1:
        #         fin_list.append(num)

        # return fin_list



sol_instance = Solution()

x = sol_instance.singleNumber([1, 2, 1, 3, 2, 5])
