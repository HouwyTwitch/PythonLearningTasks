salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

res = 0
for i in range(months):
    res += spend*((1+increase)**i)-salary
res = int(res)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", res)
