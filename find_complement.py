class Solution:
    def findComplement(self, num: int) -> int:
        _bn = str(bin(num)).split("b")[1]
        print(_bn)
        c_bn = ""
        for i in _bn:
            if i == "1":
                c_bn += "0"
            else:
                c_bn += "1"
        print(c_bn)
        c_int = int(c_bn, 2) if num > 0 else -1*int(c_bn, 2)
        return c_int
