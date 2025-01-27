class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hashmap = defaultdict(int)
        res = []

        for i in range(len(s) - 9):
            seq = s[i:i+10]
            hashmap[seq] += 1
            if hashmap[seq] == 2:
                res.append(seq)
        
        return res