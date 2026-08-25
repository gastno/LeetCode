class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        smallestMissing = k
        nums.sort()
        for num in nums:
            if(num%k == 0 and num == smallestMissing):
                smallestMissing = ((num/k)+1)*k
            elif(num%k == 0 and num > smallestMissing):
                break
        return int(smallestMissing)
