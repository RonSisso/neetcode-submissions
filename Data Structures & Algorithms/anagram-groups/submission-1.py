class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count_list = [0] * 26
            for char in s:
                count_list[ord(char) - ord('a')] += 1
            ans[tuple(count_list)].append(s)
        return list(ans.values())