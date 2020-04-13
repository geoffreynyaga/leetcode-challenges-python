# """
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process:
#     Starting with any positive integer, replace the number by the sum of the squares of its digits,
#     and repeat the process until the number equals 1 (where it will stay),
#     or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation:

# """


class Solution:
    def get_square_sum(self, array_string):
        # ["1","9"]
        # return "82"
        answer = 0

        for num in array_string:
            square = int(num) ** 2
            answer += square

        return str(answer)

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # # result = False
        # # str_num = str(n)
        # # while True:

        # #     # print(str_num, "str_num")
        # #     len_str_num = len(str_num)
        # #     split_nums_array = []

        # #     for index in range(0, len_str_num):
        # #         split_nums_array.append(str_num[index])

        # #     result = self.get_square_sum(split_nums_array)
        # #     print(result, "result")

        # #     if result == "1":
        # #         result = True
        # #         break
        # #     else:
        # #         # print("in else")
        # #         str_num = result

        # # return result

        # Solution

        # while n != 1:
        #     n = sum([int(i) ** 2 for i in str(n)])
        #     if n == 4:
        #         return False

        # return True

        #Solution
        # from math import floor, log

        # def isHappy(self, n: int) -> bool:
        #     def sum_sq_digits(num):
        #         num *= 10
        #         return sum(((num := num//10)%10)**2 for _ in range(floor(log(num, 10))+1))
        #     while (n := sum_sq_digits(n)) // 10 != 0: continue
        #     if n in {1, 7}: return True
        #     return False





sol_instance = Solution()

x = sol_instance.isHappy(19)
print(x, "x")
