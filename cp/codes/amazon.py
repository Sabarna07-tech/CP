def min_time_to_consume_items(x, y):
    if y == 0:
        return 0
    if x <= 0:
        return -1

    def simulate_with_pause(x, y, pause_time):
        total_consumed = 0
        time = 0
        current_x = x

        # Consuming till pause time
        for t in range(pause_time):
            total_consumed += current_x
            current_x *= 2
            time += 1
            if total_consumed >= y:
                return time if total_consumed == y else -1

        if total_consumed >= y:
            return -1

        # Pause for one unit time
        time += 1

        # Reset and consume after pause
        current_x = x
        while total_consumed < y:
            total_consumed += current_x
            current_x *= 2
            time += 1
            if total_consumed == y:
                return time
        
        return -1

    # First, try without any pause
    total_consumed = 0
    current_x = x
    time = 0
    while total_consumed < y:
        total_consumed += current_x
        current_x *= 2
        time += 1
        if total_consumed == y:
            return time

    min_time = float('inf')
    # Now try with different pause times
    for pause_time in range(time):
        result = simulate_with_pause(x, y, pause_time)
        if result != -1:
            min_time = min(min_time, result)

    return min_time if min_time != float('inf') else -1

# Example usage:
print(min_time_to_consume_items(2, 15))  # Output depends on the specific values of x and y