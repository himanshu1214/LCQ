
def longestCommonSubsequence(text1: str, text2: str) -> int:
    cache = {}
    def helper(text1, text2, ind):
        print(text1, text2, ind)
        if len(text1) <=0 or len(text2) <=0:
            return cache[text1[len(text1) - 1], text2[len(text2) - 1]]

        if (text1[ind], text2[ind]) in cache:
            return cache[(text1[ind], text2[ind])]

        if text1[ind] == text2[ind]:
            cache[(text1[ind], text2[ind])] = 1 + helper(text1[ind + 1:], text2[ind + 1:], ind)

        cache[(text1[ind], text2[ind])] = helper(text1[ind + 1:], text2, ind)
        cache[(text1[ind], text2[ind])] = helper(text1, text2[ind + 1:], ind)
        return cache

    helper(text1, text2, 0)


text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))
