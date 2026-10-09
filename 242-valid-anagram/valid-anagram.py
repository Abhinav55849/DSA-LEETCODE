from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq_s = Counter(s)
        freq_t = Counter(t)
        return freq_s == freq_t