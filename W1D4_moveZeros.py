# Approach #1 (Space Not-Optimal)
'''
def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    result = []
    zeros = []
    for item in nums:
        if item != 0:
            result.append(item)
        else:
            zeros.append(item)

    ans = result + zeros
    for i in range(0, len(ans)):
        nums[i] = ans[i]
'''


def moveZeroes(nums):
    '''
     !: zeroPointer
    [0,1,0,3,12]
       !
    [1,0,0,3,12]
         !
    [1,3,0,0,12]
    '''
    zeroPointer = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            # Swap Between Non-zeor element to the Zero Element Position:
            temp = nums[zeroPointer]
            nums[zeroPointer] = nums[i]
            nums[i] = temp
            print(nums)
            zeroPointer += 1
    return nums


def main():
    #print(moveZeroes([0, 1, 0, 3, 12]))
    print(moveZeroes([14, -1, 0, 3, 6, 0, -2, 0]))


if __name__ == "__main__":
    main()
