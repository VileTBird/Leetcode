class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)

        for i, c in enumerate(strs):
            key = "".join(sorted(c))
            hashmap[key].append(c)

        return hashmap.values()