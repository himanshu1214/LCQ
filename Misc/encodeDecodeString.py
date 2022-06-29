class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for i in strs:
            res += i + " ? "
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        val = []
        l_str = s.split(" ? ")
        for i in l_str[:-1]:
            val.append(i)
        return val
