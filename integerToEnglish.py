class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        
        def ones(num):
            val = {1: "One", 
                  2: "Two", 
                  3: "Three", 
                  4: "Four", 
                  5: "Five", 
                  6: "Six", 
                  7: "Seven", 
                  8: "Eight", 
                  9: "Nine"
                  }
            return val.get(num)
        
        def twos(num):
            val = {10: "Ten", 
                  11: "Eleven", 
                  12: "Twelve", 
                  13: "Thirteen", 
                  14: "Fourteen", 
                  15: "Fifteen",
                  16: "Sixteen",
                  17: "Seventeen",
                  18: "Eighteen",
                  19: "Nineteen"}
            return val.get(num)
        
        def morethannineteen(num):
            val = {2: "Twenty", 
                  3: "Thirty", 
                  4: "Forty",
                  5: "Fifty", 
                  6: "Sixty",
                  7: "Seventy",
                  8: "Eighty", 
                  9: "Ninety"}
            return val.get(num)
        
        def numtotwo(num):
            if not num:
                return ""
            elif num < 10:
                return ones(num)
            elif num < 20:
                return twos(num)
            else:
                first = num // 10
                rem = num - first*10
                return morethannineteen(first) + ' '  +  ones(rem) if rem else morethannineteen(first)
                
            
        def numIntoWords(num):
            hundred = num//100
            rem = num - hundred*100
            print(hundred, rem)
            print(numtotwo(rem))
            if hundred and rem:
                return  ones(hundred) + ' ' +  'Hundred' + ' ' + numtotwo(rem)
            elif not hundred and rem:
                return numtotwo(rem)
            elif hundred and not rem:
                return ones(hundred) + ' Hundred'
            
        billion = num//1000000000
        million = (num - billion*1000000000)// 1000000
        thousand = (num - billion*1000000000 - million*1000000)// 1000
        last_three = num - billion*1000000000 - million*1000000 - thousand*1000
        
        
        word = ""
        if billion:
            word += numIntoWords(billion) + ' Billion'
        if million:
            word += ' ' + numIntoWords(million) + ' Million' if word else '' + numIntoWords(million) + ' Million'
        if thousand:
            word += ' ' + numIntoWords(thousand) + ' Thousand' if word else '' + numIntoWords(thousand) + ' Thousand'
        if last_three:
            word += ' ' + numIntoWords(last_three) if word else '' + numIntoWords(last_three)
        return word

            
            
        
