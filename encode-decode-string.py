class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            length = str(len(s))
            res = res + length + '`' + s 
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        substring = ""
        l = 0
        length = ""
        while l < len(s):
            while s[l] != '`':
                length += s[l]
                l+=1
            
            length = int(length)
            l += 1
            while length != 0:
                substring = substring + s[l]
                length -= 1
                l+=1
            
            res.append(substring)
            substring = ""
            length = ""


        return res

