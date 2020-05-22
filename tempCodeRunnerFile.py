   while len(stones) > 1:
        max1 = -float('inf')
        max1Index = 0
        max2 = -float('inf')
        max2Index = 0
        for index, value in enumerate(stones):
            #print(f'index {index}; value: {value}')
            if value >= max1:
                max2 = max1
                max2Index = max1Index
                max1 = value
                max1Index = index
        print(f'Max1 {max1}; Max2: {max2}')
        # Delete multiple Indexes at the same time
        for index in sorted([max1Index, max2Index], reverse=True):
            del stones[index]
        if max1 != max2:
            stones.append(max1-max2)
        print(stones)
