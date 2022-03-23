class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

        roman = ''
        while num:
                        
            if num >= 3000:
                num = num % 3000
                roman += 'MMM'
                
            elif num >= 2000 and num < 3000:
                num = num % 2000
                roman += 'MM'
                
            elif num >= 1000 and num < 2000:
                num = num % 1000
                roman += 'M'
                        
            elif num >= 900 and num < 1000:
                num = num % 900
                roman += 'CM'
                
            elif num >= 500 and num < 900:
                num = num % 500
                roman += 'D'

            elif num >= 400 and num < 500:
                num = num % 400
                roman += 'CD'
                
                        
            elif num >= 300 and num < 400:
                num = num % 300
                roman += 'CCC'
                
            elif num >= 200 and num < 300:
                num = num % 200
                roman += 'CC'
                
            elif num >= 100 and num < 400:
                num = num % 100
                roman += 'C'
                
            elif num >= 90 and num < 100:
                num = num % 90
                roman += 'XC'
            
            elif num >= 50 and num < 90:
                num = num % 50
                roman += 'L'
                
            elif num >= 40 and num < 50:
                num =  num % 10
                roman += 'XL'
            
            elif num >= 30 and num < 40:
                num = num % 30
                roman += 'XXX'
                
            elif num >= 20 and num < 30:
                num = num % 20
                roman += 'XX'
                     

            elif num >= 10 and num < 40:
                num =  num % 10
                roman += 'X'

            elif num == 9:
                num = num % num
                roman += 'IX'
                
            elif num >= 5 and num < 9:
                num = num % 5
                roman += 'V'

            elif num >= 1 and num < 4:
                roman += 'I'*num
                num = num % num

            elif num == 4:
                roman += 'IV'
                num = num % num
        return roman
