import numpy as np

# генерация массива 10 на 10 случайных чисел в интервале от 1.01 до 9.99
arr = np.random.uniform(low=1.01, high=9.99, size=(10, 10))

# округление элементов массива до 2 знаков
arr = np.around(arr, decimals=2)

# вывод массива
print(f"Массив: \n{arr}")

# вывод статистической информации
print(f"\nСреднее значение: {arr.mean():.2f}")
print(f"Минимальный элемент: {np.min(arr):.2f}")
print(f"Максимальный элемент: {np.max(arr):.2f}")
print(f"Медиана: {np.median(arr):.2f}")
print(f"Стандартное отклонение: {np.std(arr):.2f}")
print(f"Дисперсия: {np.var(arr):.2f}")

# вывод диагонали массива
print(f"\nДиагональ: \n{np.diag(arr)}")
