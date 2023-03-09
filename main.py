from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
        sum = []
        
        for i in range(0, len(nums)):
            temp = 0
            temp = target - nums[i]
        
            for j in range(i+1, len(nums)):
                if temp == nums[j] :
                    sum.append(i)
                    sum.append(j)
                    break

            if len(sum) == 2 :
                break
        
        return sum
