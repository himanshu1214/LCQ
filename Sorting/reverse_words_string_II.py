class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, str):
        # write your code here
        str_list = str.split(" ")
        str_list.reverse()
        return " ".join(str_list)
