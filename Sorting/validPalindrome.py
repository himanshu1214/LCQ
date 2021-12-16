def isPalindrome(s: str) -> bool:
        ss = ""
        for i in s:
            if ord(i) > 26 or ord(i) < 126:
                ss += i
        ss = "".join(ss.split(" "))
        print(ss)
        if ss == "":
            return True

        start, end = 0, len(ss) - 1
        while start < end:
            if ss[start] == ss[end]:
                start += 1
                end -= 1
            else:

                return False
        return True
s = "race a car"
print(isPalindrome(s))
