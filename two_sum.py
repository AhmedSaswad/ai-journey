class Solution:
    def twoSum(self, nums, target):
        # Try every index i
        for i in range(len(nums)):
            # Pair it only with later indexes, so no element is used twice
            for j in range(i + 1, len(nums)):
                # Found the pair that adds up to the target
                if nums[i] + nums[j] == target:
                    return [i, j]