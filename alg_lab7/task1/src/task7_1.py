from utils import read_data_from_file, write_data_to_file

def coin_change_unlimited(money, k, coins):
    INF = float('inf')
    dp = [INF] * (money + 1)
    dp[0] = 0  
#
    for coin in coins:
        for j in range(coin, money + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    return dp[money] if dp[money] != INF else -1


def coin_change_limited(money, k, coins, counts):
    INF = float('inf')
    dp = [INF] * (money + 1)
    dp[0] = 0 

    for i in range(k):
        coin = coins[i]
        count = counts[i]

        for j in range(money, coin - 1, -1):
            for m in range(1, count + 1):
                if j - m * coin >= 0:
                    dp[j] = min(dp[j], dp[j - m * coin] + m)

    return dp[money] if dp[money] != INF else -1


def process_operations(money, k, coins, counts=None):
    if counts is None:
        result = coin_change_unlimited(money, k, coins)
    else:
        result = coin_change_limited(money, k, coins, counts)
    
    return result


if __name__ == '__main__':
    data = read_data_from_file('alg_lab7/task1/textf/input.txt')
    money, k = data[0]
    coins = data[1]
    counts = data[2] if len(data) > 2 else None
    result = process_operations(money, k, coins, counts)
    write_data_to_file('alg_lab7/task1/textf/output.txt', [str(result)])
