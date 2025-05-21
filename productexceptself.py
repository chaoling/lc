from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        brute force method would be O(N^2) timeout!
        trick: use left_prod and right_prod list to save all prod to the left and right of the current number
        and then just multiply them together to get your final answer!
        '''
        n = len(nums)
        answer = []
        left_prod = [1] * n
        right_prod = [1] * n

        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right_prod[i] = right_prod[i + 1] * nums[i + 1]

        for i in range(n):
            answer.append(left_prod[i] * right_prod[i])

        return answer

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
    print(s.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]
    print(s.productExceptSelf([1]))  # [1]
    print(s.productExceptSelf([1,2]))  # [2,1]