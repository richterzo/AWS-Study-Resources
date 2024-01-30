# control.py

# Esempi di istruzioni di controllo e cicli in Python

# Istruzione condizionale if-else
x = 10

# L'istruzione if-else è utilizzata per eseguire un blocco di codice
# se una condizione è vera, altrimenti esegue un altro blocco di codice.
if x > 5:
    print("x è maggiore di 5")
else:
    print("x non è maggiore di 5")

# Istruzione condizionale elif
y = 7

# L'istruzione elif permette di inserire una condizione aggiuntiva
# dopo un'istruzione if. Viene valutata solo se l'if precedente è falso.
if y > 10:
    print("y è maggiore di 10")
elif y > 5:
    print("y è maggiore di 5 ma non di 10")
else:
    print("y è minore o uguale a 5")

# Ciclo for
numbers = [1, 2, 3, 4, 5]

# Il ciclo for viene utilizzato per iterare su una sequenza di elementi
# come liste, tuple, stringhe, o altri oggetti iterabili.
print("Stampa dei numeri in una lista utilizzando un ciclo for:")
for num in numbers:
    print(num)

# Ciclo while
count = 0

# Il ciclo while viene utilizzato per eseguire un blocco di codice
# fintanto che una condizione specificata è vera.
print("Conteggio fino a 5 utilizzando un ciclo while:")
while count < 5:
    print(count)
    count += 1

# Esempio di break e continue all'interno di un ciclo while
print("Esempio di break e continue in un ciclo while:")
count = 0
while count < 10:
    count += 1
    if count == 3:
        print("Skip", count)
        continue  # Salta il resto del ciclo e passa alla prossima iterazione
    elif count == 8:
        print("Break", count)
        break  # Esce completamente dal ciclo
    print(count)

print("Fine")

# Esempio di nested loop (ciclo annidato)
print("Esempio di ciclo annidato:")
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")  # Stampa le coppie di valori

print("Fine")
