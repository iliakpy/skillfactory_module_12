per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

for k, v in per_cent.items():
    per_cent[k] = round(v * m)  # умножаем каждое значение из словаря на вводимое число

print("Сумма, которую вы можете заработать: ", list(per_cent.values()))

my_max_val = 0
for k,v in per_cent.items():
    if v > my_max_val:
        my_max_val=v
        my_max_key=k

print("Самый выгодный депозит в банке: ", my_max_key)

print("Сумма самого выгодного депозита: ", my_max_val)


