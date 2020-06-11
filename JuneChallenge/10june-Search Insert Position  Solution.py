"""
Search Insert Position

Solution
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
# Solution 1 : Use Linear Search

# Solution2 : Use Binary Search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        #SOL 1
        i = 0;
        l = len(nums)
        ans = 0
        while i<l and nums[i]<target:
            if nums[i]== target:
                #ans = i
                break
            if nums[i]< target:
                i=i+1
      
        return i
        '''
        # SOL 2
        l=0
        r = len(nums)
        le = len(nums)
        while l <= r: 
  
            mid = l + (r - l) // 2; 
          
        
            if nums[mid] == target: 
                return mid 
  
            # If x is greater, ignore left half 
            elif nums[mid] < target:
                if mid+1 == le or nums[mid+1]>target:
                    return mid+1
                l = mid + 1
  
            # If x is smaller, ignore right half 
            else: 
                if mid == 0 or nums[mid-1]<target:
                    return mid
                r = mid - 1

        return -1
            
