class Solution():

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = {}
        for num in nums:
            diff[num] = target - num
        for keys in diff:
            diff_1 = (target - diff[keys])
            if  diff_1 in diff.values():
                value_1 = nums.index(diff_1)
                value_2 = nums.index(diff[keys])

        print(diff)
        print(value_2,value_1)

        return [value_2, value_1]




obj1 = Solution()
print(obj1.twoSum([1,2,3,4], 6))