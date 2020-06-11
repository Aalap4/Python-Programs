# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:56:13 2020

@author: Aalap
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        dig = len(str(x))
    
        for n in range(dig//2):
            if x < 0:
                return False
            else:
                if int((x/10**(dig-n-1))%10) == int((x/10**n)%10):
                    continue
                else:
                    return False
    
        return True