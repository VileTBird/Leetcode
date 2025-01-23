class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map[s[i]]
            t_map[t[i]] = 1 + t_map[t[i]]

        for c in s_map:
            if s_map[c] != t_map[c]:
                return False
        
        return True
