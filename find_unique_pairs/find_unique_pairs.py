def find_unique_pairs(lst, target):
    unique_pairs = set()
    seen_numbers = set()
    
    for num in lst:
        complement = target - num
        
        if complement in seen_numbers:
            unique_pairs.add((min(num, complement), max(num, complement)))
        
        seen_numbers.add(num)
    
    return list(unique_pairs)

# Example usage:
input_list = [2, 4, 3, 5, 6, 7, 1, 9, 8]
target = 10
result = find_unique_pairs(input_list, target)
print(result)
