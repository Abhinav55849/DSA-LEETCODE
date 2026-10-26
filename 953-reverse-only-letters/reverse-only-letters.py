class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        p1 = 0
        p2 = len(s)-1
        while p1<p2:
            if not chars[p1].isalpha():
                p1 +=1
            elif not chars[p2].isalpha():
                p2 -=1
            else:
                chars[p1],chars[p2] = chars[p2],chars[p1]
                p1 +=1
                p2 -=1
        return "".join(chars)


            
            
        