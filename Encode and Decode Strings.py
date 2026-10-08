"""

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

"""
#this was soo easy
#just remember the opposite of ord is chr
#BEATS 99% of people so ists the best in the world!!!!!!! (hard question????)

class Solution:

    def encode(self, strs: List[str]) -> str:
        strs_encoded = ""
        for word in strs:
            for letter in word:
                new = chr(ord(letter) + 1)
                strs_encoded = strs_encoded + new
            strs_encoded = strs_encoded + " "
        print(strs_encoded)
        return strs_encoded
            

    def decode(self, s: str) -> List[str]:
        array = []
        word = ""
        for letter in s:
            if letter == " ":
                array.append(word)
                word = ""
            else:
                word = word + chr(ord(letter) - 1)
        return array