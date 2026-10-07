from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq_r = Counter(ransomNote)
        freq_m = Counter(magazine)
        return not (freq_r - freq_m)
         