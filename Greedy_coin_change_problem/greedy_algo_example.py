def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    return result if amount == 0 else []
coins = [50, 25, 10, 5, 1]  # Coin denominations in cents
amount = 77 # Amount to make change for in cents
change = greedy_coin_change(coins, amount)
print(change)