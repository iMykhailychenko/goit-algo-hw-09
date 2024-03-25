import timeit
from tabulate import tabulate


coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
            if amount == 0:
                break
    return result


def find_min_coins(amount):
    if amount == 0 or min(coins) > amount:
        return {}
    
    remaining_amount = amount

    DP = [float("inf")] * (amount + 1)
    DP[0] = 0

    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if DP[i - coin] + 1 < DP[i]:
                DP[i] = DP[i - coin] + 1
                coin_used[i] = coin

    result = {}
    remaining_amount = amount
    while remaining_amount > 0:
        coin = coin_used[remaining_amount]
        result[coin] = result.get(coin, 0) + 1
        remaining_amount -= coin

    return result


fn_map = {
    'Функція жадібного алгоритму': find_coins_greedy,
    'Функція динамічного програмування': find_min_coins,
}


if __name__ == '__main__':
    data = []

    for name, fn in fn_map.items():
        row = [name]
        for coin in [123, 1234, 12345, 1234567]:
            row.append(timeit.timeit(lambda: fn(coin), number=30))
        data.append(row)
    
    print(tabulate(data, headers=['Function', '123', '1234', '12345', '1234567'], tablefmt="pipe"))