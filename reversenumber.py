# -*- coding: utf-8 -*-
"""
Created on Fri May 29 23:57:43 2020

@author: Aalap
"""



class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            a = int('-' + x[-1:0:-1])
            
            if a >= (-2**31) and a<= (2**31-1):
                return a
            else:
                return 0
        else:
            a = int(x[::-1])
            if a >= (-2**31) and a<= (2**31-1):
                 return a
            else:
                 return 0

ob1 = Solution()
print(ob1.reverse(425))



