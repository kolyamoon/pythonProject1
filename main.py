price = []
tickets = int(input('Введите колличество билетов:'))

for i in range(1, tickets + 1):
    age = int(input(f'Введите возраст {i} покупателя:'))
    if age < 18:
        price.append(0)
    elif 18 <= age <= 25:
        price.append(990)
    else:
        price.append(1390)
if tickets > 3:
    a = sum(price) - sum(price) * 0.1
    print('Скидка покупки с учетом скидки равна:', a)
else:
    a = sum(price)
    print('Сумма вашей покупки равна:', a)
