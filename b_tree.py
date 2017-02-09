
#Dynamic Programming | Set 10 ( 0-1 Knapsack Problem)

a = [-1] * 5 * 6

def KnapSack(W, wt, val, n):
    if(n==0 or W==0):
        return 0
    if(wt[n-1] > W):
        return KnapSack(W,wt, val, n-1)
    return max(KnapSack(W,wt, val, n-1),
               val[n-1] + KnapSack(W-wt[n-1],wt, val, n-1))


def knapsack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if(i == 0 or w ==0):
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]









val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print knapsack(W , wt , val , n)
