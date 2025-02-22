def activity_selection(activities):
    """
    activities: list of tuples (start, finish)
    Returns a list of selected activities that don't overlap.
    """
    # Sort activities by their finish times
    activities.sort(key=lambda x: x[1])
    selected = []
    last_finish = -float('inf')
    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    return selected

# Example usage:
activities = [(1, 3), (2, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
print("Selected activities:", activity_selection(activities))
