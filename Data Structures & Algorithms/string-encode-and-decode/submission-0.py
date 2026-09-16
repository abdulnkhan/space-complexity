class Solution:

    def encode(self, strs: List[str]) -> str:
        """
            - We will encode in the following format: <num>#word1<num>#word2
        """
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded


    def decode(self, s: str) -> List[str]:
        """
            - We have to go through the string - extract the length
            - Append the word to a res array
            - Update the pointers to start at the next word
        """

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j+1 : j+1+length]

            res.append(word)

            i = j + 1 + length

        return res