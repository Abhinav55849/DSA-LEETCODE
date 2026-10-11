class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for word in strs:
            sorted_words = "".join(sorted(word))
            if sorted_words not in ans:
                ans[sorted_words] = []
            ans[sorted_words].append(word)
        return (list(ans.values()))