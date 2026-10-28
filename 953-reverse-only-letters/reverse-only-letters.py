class Solution(object):

  def reverseOnlyLetters(self, s):
    """

    :type s: str

    :rtype: str

    """
    s_list = list(s)
    p1 = 0
    p2 = len(s) - 1

    while p1 < p2:
      if not s_list[p1].isalpha():
        p1 += 1
      elif not s_list[p2].isalpha():
        p2 -= 1
      else:
        s_list[p1], s_list[p2] = s_list[p2], s_list[p1]
        p1 += 1
        p2 -= 1

    return "".join(s_list)