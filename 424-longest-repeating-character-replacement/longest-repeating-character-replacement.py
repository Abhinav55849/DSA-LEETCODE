class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        low = 0
        for high in range(len(s)):
            freq[s[high]] = freq.get(s[high],0) + 1

            while (high-low+1) - max(freq.values()) > k:
                freq[s[low]] -=1
                low +=1

            res = max(res,high-low+1)
        return res