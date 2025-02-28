class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 一左一右两个指针相向而行
        left, right = 0, len(s) - 1
        while left < right:
            # 交换 s[left] 和 s[right]
            temp = s[left]
            s[left] = s[right]
            s[right] = temp    
            left += 1
            right -= 1