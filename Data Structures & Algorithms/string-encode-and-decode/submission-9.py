class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = []
        for s in strs:
            res.append("&^%")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        
        s = s.split("&^%")
        return s[1:]

