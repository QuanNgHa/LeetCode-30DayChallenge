'''
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.
Contiguous subarray (containing at least one number)
For ex: [-2, 1], [-3,4,-1]

'''
# https://dev.to/13point5/maximum-subarray-3c5l

'''
Brute Force Method



def maxSubArray(nums):
    # case SubArray Length = 1
    ans = max(nums)
    # case SubArray Length > 1
    for subLength in range(2, len(nums)+1):
        # print(subLength)
        ans = max(ans, splitSubArray(ans, nums, subLength))
    return ans


def splitSubArray(ans, nums, subLength):
    # [1,2,3,4]
    # [1,2], [2,3], [3,4]

    for i in range(0, len(nums)-1):
        # print(sum(nums[i: i + subLength]))
        ans = max(ans, sum(nums[i: i + subLength]))
    # print(ans)
    return ans

'''

# https://www.youtube.com/watch?v=jnoVtCKECmQ&t=352s
# O(n) Solution:


def maxSubArray(nums):
    # When to compare a Maximum, let initial maximum value as -inf
    max_sum = -float('inf')
    current_sum = 0

    for i in range(0, len(nums)):
        current_sum += nums[i]
        if max_sum < current_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0  # Start over the new sum at the next index

    return max_sum


def main():
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    #print(maxSubArray([-2, -1]))
    # print(maxSubArray([1]))


if __name__ == "__main__":
    main()
