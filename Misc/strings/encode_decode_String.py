class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        st_ = [st + " ? " for st in strs]
        return "".join(st_)
    
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        st = s.split(" ? ")[:-1]
        return st
