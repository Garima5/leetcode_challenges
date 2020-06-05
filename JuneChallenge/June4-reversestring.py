"""
REVESRSE STRING
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
# solution logic : use a pointer from start and one from end. Move starting pointer till half and ending pointer back till half and keep replacing elements. Just keep in mind three points:
# 1. len = 0
# 2. len = even
# 3. len = odd
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        
        if l%2 == 0 and l>0:
            # Even length
            print (l)
            l1 = int(l/2)
            print (l1)
            l2 = l1-1
            i = 0
            j = l-1
            while i < l2 and j >l1:
                t = s[i]
                s[i] = s[j]
                s[j] = t
                i = i+1
                j = j-1
            t = s[l1]
            s[l1]= s[l2]
            s[l2] = t
        else:
            l1 = int(l/2)
            i = 0
            j = l-1
            while i < l1 and j> l1:
                t = s[i]
                s[i] = s[j]
                s[j] = t
                i = i+1
                j = j-1
