class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #dict which maps a set of tuples to a list of words
        
        map = {}
        temp = {}

        for word in strs:
            for char in word:
                if char in temp:
                    temp[char] += 1 
                else: temp[char] = 1
            key = tuple(sorted(temp.items()))
            if key not in map:
                map[key] = [word]
            else: map[key].append(word)
            temp.clear()

        return list(map.values())
        
        
