def main():
    salary = 5000  # зарплата
    spend = 6000  # траты
    months = 10  # количество месяцев
    increase = 0.03  # рост цен

    need_money = get_money_capital(salary, spend, months, increase)
    print(round(need_money))


def get_money_capital(salary, spend, months=10, increase=0.03):
    total_need_money = 0
    for _ in range(months):
        current_need_money = spend - salary
        total_need_money += current_need_money

        spend *= (1 + increase)

    return total_need_money

main()