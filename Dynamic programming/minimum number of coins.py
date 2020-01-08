coins = [9, 6, 5, 1]
V = 11
cache = dict()


def change(val):
    if val == 0:
        return 0, []

    if val in cache:
        print('Hit ')
        return cache[val]

    ans = float('inf')
    ans_coins = []
    for c in coins:
        if c <= val:
            ans_remaning_sum = change(val - c)
            if ans_remaning_sum[0] + 1 < ans:
                ans = ans_remaning_sum[0] + 1
                ans_coins = ans_remaning_sum[1]
                ans_coins.append(c)

    cache[val] = (ans, ans_coins)
    return ans, ans_coins


ans = change(V)
print(ans)
