#Day8  Leetcode challenge to find index of target value in a list
#https://leetcode.com/problems/two-sum/submissions/


def twoSum( nums,target):
    if len(nums) <= 10**4 and len(nums) >= 2 and target <= 10**9 and target >= -10**9:
        nl=[] 
        i=0    
        for elem in nums:
            if elem <= 10**9 and elem >= -10**9:               
                other_val = target - elem
                if other_val in nl:
                    if(elem==other_val):
                        return [index,i]
                    else:
                        return [nums.index(elem),nums.index(other_val)]
                nl.append(elem)
                if(nums.count(elem)>1):

                    index=nums.index(elem)
                i+=1
                    

print(twoSum([3,2,3],6)  )    
            
        