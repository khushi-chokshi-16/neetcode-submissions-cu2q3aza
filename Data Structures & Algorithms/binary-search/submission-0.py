class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = 0

        while low <= high:
            mid = (high + low)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid +1
            else:
                high = mid-1

        return -1
            
        

        



