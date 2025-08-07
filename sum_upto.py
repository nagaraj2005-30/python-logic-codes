def sum_upto(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_upto(5))