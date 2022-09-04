class Solution:
    def romanToInt(self, s: str) -> int:
        alp_dict = {"I": 1,
                    "IV":4,
                   "V": 5,
                    "X": 10,
                    "IX": 9,
                   "L": 50, 
                   "XL": 40, 
                   "XC": 90, 
                   "C": 100,
                   "CD": 400, 
                    "D": 500,
                   "CM": 900, 
                   "M":  1000}
        val = 0
        start = 0
        while start < len(s):
            
            if start+ 1 < len(s) and s[start] + s[start+1] in alp_dict:
                print(s[start] + s[start+1])
                val += alp_dict[s[start] + s[start+1]]
                start += 2
            else:
                val += alp_dict[s[start]]
                start += 1
        return val
