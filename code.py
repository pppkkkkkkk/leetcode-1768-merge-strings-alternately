class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i=0
        # j=0
        # result = ""
        # while i < len(word1) and j < len(word2):
        #     result = result + word1[i]
        #     result = result + word2[j]
        #     i += 1
        #     j += 1
        # while i < len(word1):
        #     result = result + word1[i]
        #     i += 1

        # while j < len(word2):
        #     result = result + word2[j]
        #     j += 1
        
        # return result

                i=0
                
        result = ""
        while i < len(word1) or  i < len(word2):
            if i < len(word1):
                result = result + word1[i]
            if i < len(word2):
                result = result + word2[i]
            i += 1
        
        return result