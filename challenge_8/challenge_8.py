import numpy as np

# Временные ряды
acceleration = np.array([3.5, 4.2, 2.8, 3.5, 4.2, 5.1, 6.2, 3.9, 4.7])
force = np.array([250, 280, 220, 290, 310, 260, 265, 270, 275])
deformation = np.array([0.02, 0.03, 0.01, 0.02, 0.03, 0.04, 0.05, 0.03, 0.02])

# Нахождение максимальных и минимальных значений и времени достижения для каждого параметра
max_acceleration = np.max(acceleration)
min_acceleration = np.min(acceleration)
time_of_max_acceleration = np.argmax(acceleration)
time_of_min_acceleration = np.argmin(acceleration)

max_force = np.max(force)
min_force = np.min(force)
time_of_max_force = np.argmax(force)
time_of_min_force = np.argmin(force)

max_deformation = np.max(deformation)
min_deformation = np.min(deformation)
time_of_max_deformation = np.argmax(deformation)
time_of_min_deformation = np.argmin(deformation)

# Вычисление площади под кривой ускорения и силы
area_acceleration = np.trapz(acceleration)
area_force = np.trapz(force)

# Вычисление среднего значения и стандартного отклонения для ускорения и силы
mean_acceleration = np.mean(acceleration)
std_acceleration = np.std(acceleration)

mean_force = np.mean(force)
std_force = np.std(force)

print("Ускорение")
print("Максимальное ускорение:", max_acceleration)
print("Время достижения максимального ускорения:", time_of_max_acceleration)
print("Минимальное ускорение:", min_acceleration)
print("Время достижения минимального ускорения:", time_of_min_acceleration)

print("\nСила")
print("Максимальная сила:", max_force)
print("Время достижения максимальной силы:", time_of_max_force)
print("Минимальная сила:", min_force)
print("Время достижения минимальной силы:", time_of_min_force)

print("\nДеформация")
print("Максимальная деформация:", max_deformation)
print("Время достижения максимальной деформации:", time_of_max_deformation)
print("Минимальная деформация:", min_deformation)
print("Время достижения минимальной деформации:", time_of_min_deformation)

print("\nИнтегральные параметры")
print("Площадь под кривой ускорения:", area_acceleration)
print("Площадь под кривой силы:", area_force)

print("\nСтатистика")
print(f"Среднее значение ускорения: {mean_acceleration:.2f}")
print(f"Стандартное отклонение ускорения: {std_acceleration:.2f}")
print(f"Среднее значение силы: {mean_force:.2f}")
print(f"Стандартное отклонение силы: {std_force:.2f}")
