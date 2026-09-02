class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        next_free = 0

        for idx in range(len(nums)): 

            if nums[idx] != val:
                if next_free != idx:
                    nums[next_free] = nums[idx]

                next_free += 1

        return next_free
        


            
                

        