"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution(object):
    def isAnagram(self, x, y):
        str1 = x  # a b c d

        str2 = y  # b c a d

        if len(str1) != len(str2):
            return False
        for index in range(len(str2)):
            val = str2[index]
            if str2[index] in str1:
                str1 = str1.replace(str2[index], "")

        if str1 == "":
            return True
        else:
            return False

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) <= 1:
            # print(strs)
            # print([strs])
            return [strs]
        checked_words = []
        # checked_words.append({"name": "tea", "value": ["ate", "eta"]},)

        for index in range(1, len(strs)):
            current_word = strs[index]
            previous_word = strs[index - 1]

            has_anagram_in_checked = False

            if len(checked_words) > 0:
                for item in checked_words:
                    # print(item["name"], "name")
                    # print(item["value"], "value")

                    if self.isAnagram(current_word, item["name"]) == True:
                        if len(item["value"]) != 0:
                            item["value"].append(current_word)
                        else:
                            item["value"].append([current_word, previous_word])

                        has_anagram_in_checked = True

            if has_anagram_in_checked == False:
                result = self.isAnagram(current_word, previous_word)

                if result == True:
                    checked_words.append(
                        {"name": current_word, "value": [current_word, previous_word]}
                    )
                else:
                    if len(strs) <= 3:

                        checked_words.append(
                            {"name": current_word, "value": [current_word]}
                        )
                        is_existing = False
                        for item in checked_words:
                            if item["name"] == previous_word:
                                is_existing = True

                        if is_existing == False:
                            checked_words.append(
                                {"name": previous_word, "value": [previous_word]}
                            )
                    else:
                        checked_words.append(
                            {"name": current_word, "value": [current_word]}
                        )

            # checked_words.append(current_word)
        final_array = []
        for obj in checked_words:
            final_array.append(obj["value"])
        return final_array


        # Solution
        # Approach 1: Categorize by Sorted String

        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()


sol_instance = Solution()

x = sol_instance.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
x1 = sol_instance.groupAnagrams(["", "b", ""])
x2 = sol_instance.groupAnagrams(["ape", "and", "cat"])


print(x, "x")
print(x1, "x1")
print(x2, "x2")
