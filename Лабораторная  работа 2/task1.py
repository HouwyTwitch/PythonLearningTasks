money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

res = money_capital
i = 0
while res > 0:
    res = money_capital+salary*i-spend*i*((1+increase)**i)
    i += 1

print("Количество месяцев, которое можно протянуть без долгов:", i)
