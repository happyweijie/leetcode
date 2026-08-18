class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Note: Same pattern as Leetcode 205 Isomorphic Strings (https://leetcode.com/problems/isomorphic-strings)

        Use dictionary to track mappings for pattern character to word
        and a set to track used words.

        No bijection if:
        1. mapping for existing character pattern[i] != words[i]
        2. words[i] is used for mapping another word
        """
        # split words into parts
        words = s.split(" ")

        # Cannot have bijection if mismatch 
        # between pattern length and no of words
        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        used_words = set()

        for p, word in zip(pattern, words):
            if p in pattern_to_word and pattern_to_word[p] != word:
                return False
                
            elif p not in pattern_to_word:
                if word in used_words:
                    return False

                pattern_to_word[p] = word
                used_words.add(word)

        return True
        