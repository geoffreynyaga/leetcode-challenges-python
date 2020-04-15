
"""
## Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""


class Solution(object):
    # def delete(self, string):
    #     str = string
    #     prev_char = []

    #     for index in range(len(string)):
    #         if index == 0 and str[index]!="#":
    #             prev_char.append(string[index])
    #         elif string[index] == "#" and len(prev_char) == 0:
    #             str = str.replace("#","",1)
    #         elif string[index] == "#":
    #             str = str.replace(prev_char[-1],"",1)
    #             str = str.replace("#","",1)
    #             prev_char.pop()
    #         else:
    #             prev_char.append(string[index])

    #     return str

    def answer(self,string):
        ans = []
        for char in string:
            if char == "#" and len(ans)==0:
                pass
            elif char == "#":
                ans.pop()
            else:
                ans.append(char)

        return "".join(ans)

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # print(self.delete(S),self.delete(T),"answers")
        print(self.answer(S),self.answer(T),"answers")


        # return self.delete(S) == self.delete(T)
        return self.answer(S) == self.answer(T)




sol_instance = Solution()

x = sol_instance.backspaceCompare("a##c", "#a#c")
x1 = sol_instance.backspaceCompare("ab##",  "c#d#")
x2 = sol_instance.backspaceCompare("a#c", "b")

x3 = sol_instance.backspaceCompare("oi###mupo##rszty#s#xu###bxx##dqc#gdjz",
"oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz"
)
print(x, "x")
print(x1, "x1")
print(x2, "x2")
print(x3, "x3")


"""
Runtime: 16 ms, faster than 89.88% of Python online submissions for Backspace String Compare.
Memory Usage: 13 MB, less than 8.00% of Python online submissions for Backspace String Compare.
"""
