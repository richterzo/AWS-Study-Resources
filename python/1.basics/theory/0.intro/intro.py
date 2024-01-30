# intro.py

# Introduzione alla programmazione in Python

# 1. Variabili e tipi di dati
# Le variabili sono contenitori per memorizzare dati.
# In Python, non è necessario dichiarare esplicitamente il tipo di variabile.
# I tipi di dati comuni includono interi, float, stringhe e booleani.

# Dichiarazione e assegnazione di variabili
age = 25            # Un numero intero
height = 1.75       # Un numero float
name = "Alice"      # Una stringa
is_student = True   # Un valore booleano

# Stampare il valore delle variabili
print("Età:", age)
print("Altezza:", height)
print("Nome:", name)
print("Studente?", is_student)

# 2. Operazioni matematiche e stringhe
# Python supporta operazioni matematiche comuni come addizione, sottrazione, moltiplicazione e divisione.
# Le stringhe possono essere concatenate utilizzando l'operatore '+'.

# Operazioni matematiche
result = age * 2 + 5
print("Risultato:", result)

# Concatenazione di stringhe
greeting = "Ciao, " + name + "!"
print(greeting)

# 3. Controllo del flusso
# Python supporta l'istruzione if-else per il controllo del flusso.
# È possibile eseguire blocchi di codice in base a condizioni specifiche.

# Istruzione if-else
if age >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")

# 4. Cicli
# Python supporta cicli for e while per eseguire azioni ripetute.
# I cicli for sono utilizzati per iterare su sequenze di elementi.
# Il ciclo while esegue un blocco di codice fintanto che una condizione è vera.

# Ciclo for
for i in range(5):   # Itera da 0 a 4
    print("Numero:", i)

# Ciclo while
count = 0
while count < 5:
    print("Conteggio:", count)
    count += 1

# 5. Funzioni
# Le funzioni sono blocchi di codice riutilizzabili.
# Accettano input, eseguono operazioni e restituiscono output opzionali.

def square(number):
    """
    Restituisce il quadrato del numero fornito.
    """
    return number ** 2

# Utilizzo della funzione square()
result = square(4)
print("Quadrato di 4:", result)

# 6. Commenti
# I commenti sono testo nel codice che viene ignorato dall'interprete Python.
# Possono essere utilizzati per fornire spiegazioni e documentazione al codice.

# Questo è un commento singolo
"""
Questo è un commento multilinea.
È utile per commentare sezioni di codice più lunghe.
"""

# Speriamo che fornisca una buona introduzione alla programmazione in Python!
