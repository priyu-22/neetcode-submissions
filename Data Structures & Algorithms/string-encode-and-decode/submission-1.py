class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode in format of [len_of_str#str]
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            word = s[i:j]
            res.append(word)
            i = j
        return res
        
'''
dry run:
 encoded string - 
"5#Hello5#World"
 i
  j == # -> length: s[i:j] = 5
   i -- i = j+1
        j = i+ length = 2+5 = 7th index as we want to calculate next word/str
        word = s[i:j] = Hello
        i = j
'''
