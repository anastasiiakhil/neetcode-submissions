class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = [None] * 2 * len(nums)

        for i in range(len(ans)):
            ans[i] = nums[-(len(nums)-i)]
        
        return ans
