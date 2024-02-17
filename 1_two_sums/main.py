#!/usr/bin/env python
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
import sys
import pdb
from typing import List

class Solution:
    def primitive_lookup(self, num: list, target: int):
        """
        Fails, num is not a list of unique items
        fails on [3, 3] 6
        """
        num = [int(i) for i in num]
        table = {v: i for i, v in enumerate(num)}

        for el in num:
            search = target - el
            if el == search:
                continue

            try:
                return [table[el], table[search]]
            except:
                continue

        return None

    def bruteforce_check_right(self, num: list, target: int):
        """
        Bruteforce, O(n**2) - about 65ms on leetcode
        """
        num = [int(i) for i in num]

        for el_i, el in enumerate(num):
            search = target - el
            for _i, _el in enumerate(num):
                if search == _el and _i != el_i:
                    return [el_i, _i]


        return None

    def traverse_map(self, num: List[int], target: int):
        """
        Optimized solution - about 55ms on leetcode
        """
        map_ = {}

        for idx, el in enumerate(num):
            search = target - el
            if search in map_:
                return [map_[search], idx]

            map_[el] = idx


    def twoSum(self, *args, **kwargs):
        return self.traverse_map(*args, **kwargs)


if __name__ == '__main__':
    print(
        Solution().twoSum(
            [int(i) for i in sys.argv[1:-1]],
            int(sys.argv[-1])
        )
    )
