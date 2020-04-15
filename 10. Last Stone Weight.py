"""
Last Stone Weight
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        sorted_stones = stones
        print(sorted_stones, "stones")

        for index in range(len(stones) - 1):
            sorted_stones = sorted(sorted_stones)

            sorted_stones.append(sorted_stones.pop() - sorted_stones.pop())

            # print(index)
            # if stones[index] % 2 !=0:
            # diff = sorted_stones[index] - sorted_stones[index - 1]
            # sorted_stones[index - 1] = 0
            # sorted_stones[index] = diff

            # sorted_stones = sorted(sorted_stones, reverse=True)
            print(sorted_stones, "ccccccc")

            # sorted_stones.remove([sorted_stones[index], sorted_stones[index - 1]])
            # sorted_stones.append(diff)
        # sorted_stones.remove(0)
        print(sorted_stones)
        return sorted_stones[0]


sol_instance = Solution()

x = sol_instance.lastStoneWeight([2, 7, 4, 1, 8, 1])


print(x, "x")
