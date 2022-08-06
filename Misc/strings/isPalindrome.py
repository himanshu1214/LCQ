    def isPalindrome(self, s: str) -> bool:

        
        new_s = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                new_s += i.lower()

        if not new_s:
            return True

        mid = len(new_s) // 2
        if len(new_s) % 2 == 0: # even
            start, end = mid-1, mid
        if len(new_s) % 2 == 1: # odd
            start, end = mid-1, mid + 1
                
        while start >= 0 and end <len(new_s):
            if new_s[start] == new_s[end]:
                start -= 1
                end += 1
            else:
                return False
            
        return True
