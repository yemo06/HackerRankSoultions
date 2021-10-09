#You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
#On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day.

#Find and return the maximum profit you can achieve.

def maxProfit(prices):
    if (len(prices)==1):
        return 0
    else:
        maxsum = 0
        for i in range(len(prices)-1):
                if (prices[i+1]>prices[i]):
                    maxsum += prices[i+1] - prices[i]
                # else:
                #     continue
    
    return maxsum