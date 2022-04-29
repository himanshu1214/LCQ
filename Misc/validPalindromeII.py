class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        del_counter = 0
        lst_del_elm_st = 0
        lst_el_end = 0
        while start <= end:
            print(start, end)
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                del_counter += 1
                if del_counter == 1:
                    lst_del_elm_st, lst_el_end = start, end
                    start += 1
                elif del_counter == 2:
                    start, end = lst_del_elm_st, lst_el_end
                    end -= 1
                else:
                    return False
 
        return True
                    
                
