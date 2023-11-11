try:
    transactions = []
    user_stats = {}
    while True:
        user_id = int(input("Write user ID (0 to stop): "))
        if user_id == 0:
            break
        transaction_type = int(input("Write transaction (1-comment, 2-like, 3-share): "))
        transactions.append((user_id, transaction_type))
    for user_id, transaction_type in transactions:
        if user_id not in user_stats:
            user_stats[user_id] = {1: 0, 2: 0, 3: 0}
        user_stats[user_id][transaction_type] += 1
    for user_id, stats in user_stats.items():
        most_frequent = max(stats, key=stats.get)
        least_frequent = min(stats, key=stats.get)
        stats['mft'] = most_frequent
        stats['lft'] = least_frequent
    for user_id, stats in user_stats.items():
        print(f"User ID: {user_id}, Statistics: {stats}")
except (ValueError, IndexError):
    print("Wrong value or sequence out of range!!!")