# variables.py

"""
Introduzione alle variabili in Python:

Le variabili sono elementi fondamentali nella programmazione Python.
Sono contenitori che consentono di memorizzare dati, come numeri, stringhe e oggetti.

In Python, le variabili sono dinamicamente tipizzate, il che significa che non è
necessario specificare il tipo di dato quando si dichiara una variabile.

Iniziamo con un classico "Hello, world!" per dare il benvenuto al mondo delle variabili.
"""

# Stampa del messaggio di benvenuto
print("Benvenuto nel mondo delle variabili in Python!")

# Definizione e utilizzo delle variabili
x = 5           # Variabile intera
y = 3.14        # Variabile float
name = "John"   # Variabile stringa
is_true = True  # Variabile booleana

# Stampa dei valori delle variabili
print("Valore di x:", x)
print("Valore di y:", y)
print("Nome:", name)
print("is_true:", is_true)

# Modifica dei valori delle variabili
x = 10
y = 2.71
name = "Alice"
is_true = False

# Stampa dei nuovi valori delle variabili
print("Nuovo valore di x:", x)
print("Nuovo valore di y:", y)
print("Nuovo nome:", name)
print("Nuovo is_true:", is_true)

# Python consente di ottenere informazioni sulle variabili utilizzando la funzione `type()`
# che restituisce il tipo di dato della variabile.
print("Tipo di x:", type(x))
print("Tipo di y:", type(y))
print("Tipo di name:", type(name))
print("Tipo di is_true:", type(is_true))

# È possibile ottenere anche la dimensione occupata in memoria da una variabile usando
# la funzione `sys.getsizeof()` dal modulo `sys`.
# la funzione restituisce il numero di byte occupati da quell'oggetto nella memoria.
import sys

print("Dimensione di x (in byte):", sys.getsizeof(x))
print("Dimensione di y (in byte):", sys.getsizeof(y))
print("Dimensione di name (in byte):", sys.getsizeof(name))
print("Dimensione di is_true (in byte):", sys.getsizeof(is_true))

# Python è un linguaggio a tipizzazione dinamica, il che significa che una variabile può contenere
# un diverso tipo di dato rispetto al suo valore precedente.
# Ad esempio:
x = "Hello"
print("Valore di x dopo aver cambiato il tipo:", x)