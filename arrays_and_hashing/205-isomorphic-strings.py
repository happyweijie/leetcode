class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # redundant check for this problem since s and t have equal lengths
        if len(s) != len(t):
            return False

        #  mapping from character in s to its replacement in t
        replacements = {}
        taken = set() # letters in t that were already used to replace some characters in s
        
        for cs, ct in zip(s, t):
            #  return False if cs already has a replacement that is not ct
            # two characters in t cannot map to same character in s
            if cs in replacements and ct != replacements[cs]:
                return False
            elif cs not in replacements:
                # return False if ct is already used to replace some char in s
                if ct in taken:
                    return False
                
                # found a replacement for that particular character in s
                replacements[cs] = ct
                taken.add(ct)

        return True
        