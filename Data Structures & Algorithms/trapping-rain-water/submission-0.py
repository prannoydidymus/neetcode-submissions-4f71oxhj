class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return False
        left,right = 0,len(height)-1
        lmax,rmax = height[left],height[right]
        trapped = 0

        while left < right:
            if lmax < rmax:
                left +=1
                lmax = max(lmax,height[left])
                trapped += lmax - height[left]
            else:
                right -=1
                rmax = max(rmax,height[right])
                trapped += rmax - height[right]
        return trapped