import numpy as np

# Генерация случайных данных о продажах
years = np.random.choice(range(2011, 2023), size=100000)
sales = np.random.randint(500, 125000, size=100000)
revenue = np.random.randint(1000000, 50000000, size=100000)

sales_data = np.column_stack((years, sales, revenue))

# Находим общее количество продаж за каждый год
total_sales_by_year = np.zeros((12,))
for i in range(12):
    total_sales = np.sum(sales_data[sales_data[:, 0] == (2011 + i), 1])
    total_sales_by_year[i] = total_sales

print("Общее количество продаж")
for i, year in enumerate(range(2011, 2023)):
    print(f"в {year} году: {int(total_sales_by_year[i])}")

# Вычисляем среднюю выручку от продажи за каждый год
average_revenue_by_year = np.zeros((12,))
for i in range(12):
    average_revenue = np.mean(sales_data[sales_data[:, 0] == (2011 + i), 2])
    average_revenue_by_year[i] = average_revenue

print("\nСредняя выручка")
for i, year in enumerate(range(2011, 2023)):
    print(f"в {year} году: {average_revenue_by_year[i]:.2f}")

# Определяем год с максимальным количеством продаж
max_sales_year = sales_data[:, 0][np.argmax(sales_data[:, 1])]
print(f"\nГод с максимальным количеством продаж: {max_sales_year}")

# Определяем год с минимальной выручкой от продажи
min_revenue_year = sales_data[:, 0][np.argmin(sales_data[:, 2])]
print(f"Год с минимальной выручкой от продаж: {min_revenue_year}")
