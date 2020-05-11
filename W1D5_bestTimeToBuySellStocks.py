def maxProfit(prices):
    # print(prices)
    maxProfit = 0
    valley = prices[0]
    peak = prices[0]
    i = 0

    # O(n) as only loop with i
    while(i < len(prices)-1):
        # Step 1: Find the valley
        while((i < len(prices)-1)and prices[i] >= prices[i+1]):
            i += 1
        valley = prices[i]
        # Step 2: Find the peak
        while((i < len(prices)-1)and prices[i] <= prices[i+1]):
            i += 1
        peak = prices[i]

        maxProfit += peak - valley

    return maxProfit


def main():

    print(maxProfit([1, 2, 3, 4, 5]))  # O/P: 4
    #print(maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == "__main__":
    main()
