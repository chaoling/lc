'''
Coins in a Line 1
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.
Could you please decide the first play will win or lose? Example n = 1, return true.
n = 2, return true.
n = 3, return false.
n = 4, return true. n = 5, return true.
'''
def coins(n: int) -> bool:
    '''
    strategy: dp[i] stands for the best move for player 1 to win
    n = 1 or 2: True
    n = 3: False since player 1 can only take 1 or 2, but either way it left 1 or 2 for opponents
    so winning condition is : the last move for player 1 left is 1 or 2
    just do it backwards
    each step player can choose 1 or 2, so the power set is 2^N
    can we use dynamic programming to reduce the workload?
    
    dp[i] means for ith coin total, can player 1 win?
    dp[1] = dp [2] = True #1 or 2 coins player 1 will win
    dp[3] = False since there are 1 coin or 2 coin left for opponent
    dp[4] = True since dp[2] is true and dp[3] is false
    so let's look at the previous coin:
    1 win, 2 win, 3 lose , 4 win 
    if dp[i-1] lose, dp[i] will win
    if dp[i-2] lose, dp[i] will also win?

    dp[i] = not dp[i-1] or not dp[i-2]
    '''
    # edge case
    if n == 0:
        return False
    if n == 1 or n == 2:
        return True
    
    dp = [1, 1]
    for i in range(2, n):
        #player can win only if dp[i-1] or dp[i-2] can not win
        if not dp[-1] or not dp[-2]:
            dp.append(1)
        else:
            dp.append(0)
    
    return dp[-1] == 1

if __name__=="__main__":
    for i in range(1,10):
        print(f"{i} coin: result: {coins(i)}")

