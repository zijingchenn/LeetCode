class Solution:
    # 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串
    def palindrome(self, s: str, l: int, r: int) -> str:
        # 防止索引越界
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 双指针，向两边展开
            l -= 1
            r += 1
        # 返回以 s[l] 和 s[r] 为中心的最长回文串
        return s[l + 1: r]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(0, len(s)):
            # 以 s[i] 为中心的最长回文子串
            s1 = self.palindrome(s, i, i)
            # 以 s[i] 和 s[i+1] 为中心的最长回文子串
            s2 = self.palindrome(s, i, i + 1)
            # res = longest(res, s1, s2)
            res = s1 if len(res) < len(s1) else res
            res = s2 if len(res) < len(s2) else res
        return res