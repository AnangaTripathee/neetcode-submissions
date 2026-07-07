class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Step 1: output[i] = product of all elements before i
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i - 1]

        # Step 2: multiply by product of all elements after i
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output