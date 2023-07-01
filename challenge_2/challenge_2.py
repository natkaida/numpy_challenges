import numpy as np

# Данные о прокате велосипедов за каждый месяц сезона
spring_rentals = np.array([11362, 11489, 12842])
summer_rentals = np.array([15401, 16562, 17728])
autumn_rentals = np.array([14994, 13851, 12784])
winter_rentals = np.array([840, 950, 1210])

# Вычисление общего количества прокатов велосипедов для каждого сезона
total_spring_rentals = np.sum(spring_rentals)
total_summer_rentals = np.sum(summer_rentals)
total_autumn_rentals = np.sum(autumn_rentals)
total_winter_rentals = np.sum(winter_rentals)

# Вычисление среднего количества прокатов велосипедов для каждого сезона
average_spring_rentals = np.mean(spring_rentals)
average_summer_rentals = np.mean(summer_rentals)
average_autumn_rentals = np.mean(autumn_rentals)
average_winter_rentals = np.mean(winter_rentals)

# Создание массива средних значений
average_rentals = np.array([average_spring_rentals, average_summer_rentals, average_autumn_rentals, average_winter_rentals])

# Определение самого прибыльного сезона
most_profitable_season = np.argmax(average_rentals)

seasons = ['весна', 'лето', 'осень', 'зима']
print(f"Самый прибыльный сезон - {seasons[most_profitable_season]}")
