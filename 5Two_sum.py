# return indices of the two numbers such that they add up to target python
def twoSum(self, nums, target):
        dictionary = {}
        answer = []
        
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
                
            dictionary.update({nums[i]: i})