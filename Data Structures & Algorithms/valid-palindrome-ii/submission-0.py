class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j  = 0, len(s)-1
        count =0
        for c in s:
            while i < j:
                if s[i] == s[j]:
                    i +=1
                    j-=1
                elif count==0:
                    if(s[i]==s[j-1]):
                        j-=1
                        count = 1
                    elif(s[i+1]==s[j]):
                        i+=1
                        count=1
                    else:
                        return False
                else:
                    return False
        return True

        