class Solution:
    def reverseString(self, s: List[str]) -> None:
        a = []
        for i in range(len(s)-1,-1,-1):
            a.append(s[i])
        for i in range(len(s)):
            s[i] = a[i]      