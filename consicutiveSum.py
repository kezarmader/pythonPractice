'''
Given an integer array nums, find  contiguous max subarray sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
'''
def main():
    nums = [1,1,-1,-1,-1,-1,1,1,1]
        
    sum = 0
    maxSum = float('-inf')
    for i in range(len(nums)):
        sum = max(nums[i], sum + nums[i])
        maxSum = max(maxSum, sum)
    
    print(maxSum)

if __name__ == '__main__':
    main()
    