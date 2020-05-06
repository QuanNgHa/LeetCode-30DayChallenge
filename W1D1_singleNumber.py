# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
'''
Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
'''

# Approach 1: List operation
from collections import defaultdict


def singleNumberApproach1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_duplicate_list = []
    for num in nums:
        if num not in no_duplicate_list:
            no_duplicate_list.append(num)
        else:
            no_duplicate_list.remove(num)
    return no_duplicate_list.pop()


print(singleNumberApproach1([4, 1, 2, 1, 2]))

# Approach 2: Hash Table


def singleNumberApproach2(nums):
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1

    for i in hash_table:
        if hash_table[i] == 1:
            return i


print(singleNumberApproach2([4, 1, 2, 1, 2]))
