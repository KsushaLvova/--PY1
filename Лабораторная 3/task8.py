def main():
    money_capital = 10000
    salary = 5000
    spend = 6000
    increase = 0.05
    result = task1(money_capital, salary, spend, increase)

    print(result)

def task1(money_capital, salary, spend, increase=0.05):
    month = 0  # количество месяцев, которое можно прожить
    while True:
        delta = spend - salary # вычисляем разницу за месяц
        if delta > money_capital:
            break
        money_capital -= delta # уменьшается подушка безопастности
        month += 1
        spend = spend + (spend * increase)
    return month
def task2(money_capital, salary, spend, increase=0.05):
    month = 0  # количество месяцев, которое можно прожить
    while True:
        if spend > money_capital:
            break
        money_capital = money_capital - spend + salary  # уменьшается подушка безопастности
        month += 1
        spend *= 1 + increase
        return month
main()
