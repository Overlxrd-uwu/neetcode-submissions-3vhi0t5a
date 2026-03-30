class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for s in strs:
            news = "".join(sorted(s))
            table[news].append(s)

        return list(table.values())
   