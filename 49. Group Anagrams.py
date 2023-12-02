class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}
        
        for i in strs:
            if tuple(sorted(i)) not in hm:
                hm[tuple(sorted(i))] = [i]
            else:
                hm[tuple(sorted(i))].append(i)
        
        return hm.values()
        