import numpy_financial as npf
import numpy as np

# Заданные параметры кредита
annual_interest_rate = 0.12
loan_amount = 5000000
loan_term = 3

# Расчет месячной процентной ставки и общего количества платежей
monthly_interest_rate = annual_interest_rate / 12
total_payments = loan_term * 12

# Расчет аннуитетного платежа
annuity_payment = npf.pmt(monthly_interest_rate, total_payments, -loan_amount)

# Расчет дифференцированного платежа
principal_payment = loan_amount / total_payments

# Расчет оставшейся суммы кредита для каждого месяца
remaining_loan_amounts = loan_amount - np.arange(total_payments) * principal_payment

# Расчет процентных платежей
interest_payments = remaining_loan_amounts * monthly_interest_rate

# Расчет дифференцированных платежей
differentiated_payments = principal_payment + interest_payments


# Вывод заголовка таблицы
print(f"{'Платеж':<10}{'Аннуитетный':<15}{'Дифференцированный':<15}")

# Вывод строк таблицы для каждого платежа
for i, payment in enumerate(differentiated_payments, 1):
    print(f"#{i:<9}{round(annuity_payment, 2):<15}{round(payment, 2):<15}")

# Расчет общих затрат на погашение кредита для аннуитетного и дифференцированного способов
total_cost_annuity = annuity_payment * total_payments
total_cost_differentiated = sum(differentiated_payments)

# Вывод общих затрат на погашение кредита
print(f"\nПереплата при аннуитетном погашении: {round(total_cost_annuity - loan_amount, 2)}")
print(f"Переплата при дифференцированном погашении: {round(total_cost_differentiated - loan_amount, 2)}")
