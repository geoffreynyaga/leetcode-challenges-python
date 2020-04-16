"""
Perform String Shifts
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.



Example 1:

Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
Example 2:

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


Constraints:

1 <= s.length <= 100
s only contains lower case English letters.
1 <= shift.length <= 100
shift[i].length == 2
0 <= shift[i][0] <= 1
0 <= shift[i][1] <= 100
   Hide Hint #1
Intuitively performing all shift operations is acceptable due to the constraints.
   Hide Hint #2
You may notice that left shift cancels the right shift, so count the total left shift times (may be negative if the final result is right shift), and perform it once.
"""


class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """

        direction = None
        count = 0

        for arr in shift:
            if arr[0] == 0:
                count += arr[1]
            else:
                count -= arr[1]

        if count == 0:
            return s
        elif count > 0:
            if count > len(s):
                count = count % len(s)

            print(count, "count +")
            print(s[:count], "s[:count] +")
            print(s, "s")

            old_str = s
            print(old_str.replace(s[:count], "", 1), "replace")
            new_s = old_str.replace(s[:count], "", 1) + s[:count]
            return new_s
        else:
            if abs(count) > len(s):
                count = -(abs(count) % len(s))

            print(count, "count - ")
            print(s[count:], "s[: abs(count)] ")
            print(s.replace(s[count:], ""), "s.replace(s[: abs(count)] ")

            new_s = s[count:] + s.replace(s[count:], "", 1)
            print(new_s, "new_s")
            return new_s


sol_instance = Solution()

x = sol_instance.stringShift(
    "yzeuobhwxatulpruiab",
    [
        [1, 15],
        [0, 18],
        [0, 12],
        [0, 7],
        [0, 7],
        [1, 17],
        [1, 15],
        [0, 9],
        [1, 4],
        [0, 19],
        [1, 16],
        [0, 7],
        [1, 4],
        [1, 17],
        [1, 19],
        [1, 10],
        [1, 2],
        [0, 18],
        [1, 15],
    ],
)
print(x, "x")
