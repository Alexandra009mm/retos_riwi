def calculate_total(items):
    total = 0
    for sal in items:
        total += sal["subtotal"]

    return total