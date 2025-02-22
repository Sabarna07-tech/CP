def fractional_knapsack(values, weights, capacity):
    """
    values: list of item values
    weights: list of item weights
    capacity: maximum weight the knapsack can carry
    Returns the maximum total value achievable.
    """
    # Pair each value with its weight and sort by ratio (value/weight) in descending order
    items = list(zip(values, weights))
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    print(items)
    total_value = 0.0
    for value, weight in items:
        if capacity == 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            # Take the fraction that fits in the remaining capacity
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0
    return total_value

# Example usage:
values = [60, 100, 120, 50]
weights = [10, 20, 30, 25]
capacity = 60
print("Maximum value:", fractional_knapsack(values, weights, capacity))
