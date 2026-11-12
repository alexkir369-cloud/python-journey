def calc_tip(bill, percent):
    return bill * percent / 100


def show_tips(bill):
    for percent in [10, 15, 20]:
        tip = calc_tip(bill, percent)
        print(f"{percent}% от счёта:", tip)
        print("Всего:", bill + tip)


answer = input("Сумма счёта? ")
bill = float(answer)

if bill > 100:
    print("Большой счёт")
else:
    print("Счёт в норме")

show_tips(bill)