class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [2,2,2, 5,5,5, 3]
        # set_nums = [2, 5, 3] x 3  - nums = value*2

        set_nums = set(nums)  # 2,3,
        value = ((3 * (sum(set_nums))) - sum(nums)) / 2

        print(value, "value")

        return value


sol_instance = Solution()

x = sol_instance.singleNumber([2, 2, 3, 2])

print(x, "x")


# return(2*sum(set(nums))-sum(nums))
