def optimal_card_stacking(card_values):
    n = len(card_values)
    dp = [0] * n
    
    # Calculate maximum sum for each index
    for i in range(n):
        dp[i] = card_values[i]
        for j in range(i):
            if card_values[i] > card_values[j]:
                dp[i] = max(dp[i], dp[j] + card_values[i])
    
    # Find the maximum sum in dp array
    max_sum = max(dp)
    return max_sum

# Example usage
card_values = [4, 10, 7, 1, 3, 8, 5, 6, 9, 2]
result = optimal_card_stacking(card_values)
print("Maximum sum of card values:", result)
