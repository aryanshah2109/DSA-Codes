# Leetcode 121
import numpy as np

def buySellStocksBrute(arr):

    n = len(arr)

    maxProfit = 0

    for i in range(n):
        diff = 0
        for j in range(i+1,n):
            
            diff = arr[j] - arr[i]

            maxProfit = max(diff, maxProfit)

    return maxProfit

def buySellStocksOptimal(arr):
    # Optimal TC = O(n) SC = O(1)
    n = len(arr)
    profit = 0
    minSubarray = arr[0]

    for i in range(1, n):

        cost = arr[i] - minSubarray

        profit = max(profit, cost)

        minSubarray = min(minSubarray, arr[i])

    return profit
            
arr = np.fromstring(input("Enter array elements: "),sep=" ", dtype=np.int32)

print(buySellStocksBrute(arr))
print(buySellStocksOptimal(arr))