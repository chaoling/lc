from typing import List


def trap(self, height: List[int]) -> int:
        '''
        for each location/cell, look to the left and look to the right,
        if the elevation is higher than current cell, aka height[left]> height[curr]
        and the elevation of right is higher too, then it can trap water?
        as long as 
        '''
        n = len(height)
        #L[i] is the tallest bar from left up to i
        L,R =[0]*n,[0]*n
        L[0] = height[0]
        R[n-1] = height[n-1]
        for i in range(1,n):
            L[i] = max(L[i-1],height[i])
        for j in range(n-2,-1,-1):
            R[j] = max(R[j+1],height[j])
        
        water = 0
        for i in range(n):
            water += max(0, min(L[i], R[i]) - height[i])
        return water

def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        left_max = right_max = 0
        water = 0

        '''
        Sweep inward
        While l <= r:

        Compare the bars at l and r:

        If height[l] <= height[r], then the left side is the bottleneck—everything to the right is at least as tall as height[l], so we know the highest wall on the right is ≥ height[r] ≥ height[l].
        '''

        while l <= r:
            if height[l] <= height[r]:
                # left is the lower boundary
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                # right is the lower boundary
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1

        return water