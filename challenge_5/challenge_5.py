import numpy as np

print("Прошлая доходность акций")
# Прошлая доходность акций (в процентах за период)
returns = np.array([float(element) for element in input().split(",")])

print("Стандартное отклонение акций")
# Стандартное отклонение акций (в процентах)
std_devs = np.array([float(element) for element in input().split(",")])

print("Сумма")
# Сумма, которой располагает инвестор
invest_amount = int(input())

print("Допустимый уровень риска")
# Допустимый уровень риска портфеля (в процентах)
risk_level = int(input())

# Вычисление взвешенной средней доходности портфеля
print("Доли акций в портфеле")
weights = np.array([float(element) for element in input().split(",")])
portfolio_returns = np.dot(returns, weights)

# Вычисление стандартного отклонения портфеля
portfolio_std_dev = np.sqrt(np.dot(weights, np.dot(std_devs, weights.T)))

# Проверка уровня риска портфеля
if (portfolio_std_dev <= risk_level).any():
    print("Уровень риска портфеля соответствует требованиям.")
else:
    print("Уровень риска слишком высок. Рекомендуем изменить веса акций в портфеле.")
