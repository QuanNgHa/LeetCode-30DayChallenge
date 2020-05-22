# Soln 1: 2 pointers approach
# def lastStoneWeight(stones):
# Check if List contains only 1 element:
#    if len(stones) == 1:
#         return stones[0]
#     while len(stones) > 1:
#         max1 = -float('inf')
#         max1Index = 0
#         max2 = -float('inf')
#         max2Index = 0
#         for index, value in enumerate(stones):
#             # print(f'index {index}; value: {value}')
#             if value >= max1:
#                 max2 = max1
#                 max2Index = max1Index
#                 max1 = value
#                 max1Index = index
#             elif value >= max2:
#                 max2 = value
#                 max2Index = index
#         print(f'Max1 {max1}; Max2: {max2}')
#         # Delete multiple Indexes at the same time
#         for index in sorted([max1Index, max2Index], reverse=True):
#             del stones[index]
#         if max1 != max2:
#             stones.append(max1-max2)
#         print(stones)
#     if (stones):
#         return stones[0]
#     else:
#         return 0

# Soln 2: Optimized Soln 1 with Python Build-in functions of List
# Max() and Remove()


def lastStoneWeight(stones):
    while len(stones) != 0:
        if len(stones) == 1:
            return stones[0]
        else:
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            stones.remove(max2)

            if max1 > max2:
                stones.append(max1-max2)
    return 0


if __name__ == '__main__':
    # lastStoneWeight([2, 7, 4, 1, 8, 1])
    # lastStoneWeight([3, 1])
    print(lastStoneWeight([2, 2]))
    # lastStoneWeight([9, 3, 2, 10])
