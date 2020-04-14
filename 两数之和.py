class Solution:
    def twoSum(self, nums, target):
        i = 0
        for x in nums:
            c = 0
            for y in nums[i:len(nums)]:
                j = i+c
                if x + y == target:
                    print([i,j])
                    return
                c+=1
            i += 1       
s = Solution()
s.twoSum([2,7,11,15],18)