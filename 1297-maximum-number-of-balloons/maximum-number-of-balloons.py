from collections import Counter

class Solution(object):
    def maxNumberOfBalloons(self, text):
        
        counter_text = Counter(text)
        balloon = Counter("balloon")
        res = len(text)

        for char in balloon:
            res = min(res, counter_text[char] // balloon[char])
        return res
