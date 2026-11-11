name ="Alex"
bill= 45.50
guessts = 3
answer = input ("Сумма счёта? ")
bill = float (answer)
if bill > 100 :
    print ("Большой счет")
else:
    print ("Счёт в норме")  
for percent in [ 10,15,20]:
        
    tip = bill * percent / 100
    print(f"{percent}% от счёта:", tip)
    print("Всего:", bill + tip)

           