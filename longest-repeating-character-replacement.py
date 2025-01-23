class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxLength = 0
        l = 0
        hash_table = defaultdict(int)
        
        for i in range(len(s)):
            hash_table[s[i]] = hash_table[s[i]] + 1

            if ((i - l + 1) - max(hash_table.values()) > k):
                hash_table[s[l]] = hash_table[s[l]] - 1
                l = l + 1
                
                
            maxLength = max(maxLength, i - l + 1)

        return maxLength 

        


            
            
        