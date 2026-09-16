class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        res = 5#Hello5#World
        """
        res = ''
        for word in strs:
            length = str(len(word))
            res  += length + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            res.append(word)
            i = j+1+length
        return res