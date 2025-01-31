'''
Chose an easy problem cus mybrains fried, this is the last one for today.

basically when numerals are placed in descending order we add
for example VI = 5 + 1 = 6

on the other when a small number appears before a larger number we subtract
for example IV = 1 - 5 = 4

thats pretty much it u basically check if the current numeral at ith index in the string s, is smaller than the following numeral
if it is we decrement it by the corresponding number, for example if its IV and i is at I then we subtract 1 from result

on the other hand if its the opposite or else, then we add the following numeral to result

when its all over the result should add and subtract upto the corresponding value of the given roman numerals.

'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {"I":  1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}

        res = 0

        for i in range(len(s)):
            if i < len(s) - 1 and hashmap[s[i]] < hashmap[s[i+1]]:
                res -= hashmap[s[i]]
            else:
                res += hashmap[s[i]]

        return res
        