'''
Man I hate this problem. so convoluted. 

my initial solution was to basically start with sorting p, then iterating thru s, while sorting each window in s and comparing with p
essentially this would involve a time complexity of o(n * k^2) where k = len(p) the solution isnt that bad assuming p is always 
smaller than s, which is an edge case i ofc forgot but essentially its not that efficient. mainly due to the fact that 
we sort a string wiht the len(p) over and over again 

the actual or most efficient solution wouldbe to ofc checking for the edge case where if len(P)> len (s) if true we return empty array

if not we move on, we initialize two hashmaps, sure the hashmap would casue a memory complexity of o(k^2) but its better than the 
initial solution due to the improvement in time complexity. this is many because each time we compare a window of s to p,
we essentially compare the count of characters, in the english alphabet there are 26 characters which would be each time o(26)
but before we were looping thru the entire window where p could have a thousand characters, sorting that is very inefficient

after we check the edge case, we basically start with storing the count of each character in the p string, and we store each
character from string s or the first window, if theyre equal we append 0 to res if not we just leave an empty array

in the following loop we basically iterate from a range of (length p to length of s) cus we already added the initial window
and compared it. 
at the start of the array we add the right most pointer to our hashmap and decrement the count of the left most character
which is straightforward as the window slides. 
if the leftmost character has a count of 0 it could skew the comparison so we pop the key for the left most character,
then we increment our left pointer by 1 and after that we just compare the two window hashmaps if theyre equal we just add the left
pointer position to our res array

finally return res array
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        res = []

        p_map = defaultdict(int)
        s_map = defaultdict(int)

        for i in range(len(p)):
            p_map[p[i]] += 1
            s_map[s[i]] += 1

        res = [0] if s_map == p_map else []

        l = 0
        for r in range(len(p), len(s)):
            s_map[s[r]] += 1
            s_map[s[l]] -= 1

            if s_map[s[l]] == 0:
                s_map.pop(s[l])
            l+=1
            if s_map == p_map:
                res.append(l)

            

        return res 