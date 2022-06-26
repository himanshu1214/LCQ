class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [i.lower() for i in s if i.isalpha() or i.isdigit()]

        s_str = "".join(s)
        mid = len(s_str)//2
        ptr1 = mid-1 if len(s_str) % 2 == 0 else mid
        ptr2 =  mid if len(s_str) % 2 == 0 else mid
        
        print(ptr1, ptr2)
        while ptr1 >= 0 and ptr2 < len(s_str):
            if s_str[ptr1] != s_str[ptr2]:
                return False
            
            ptr1 -= 1
            ptr2 += 1
            
        return True
