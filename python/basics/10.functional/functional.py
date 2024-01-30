# Programmazione funzionale

# Utilizzo di lambda function per definire funzioni anonime
addition = lambda x, y: x + y  # Definizione di una funzione lambda per l'addizione
print("Somma:", addition(3, 5))  # Utilizzo della funzione lambda per sommare due numeri

# Utilizzo di map per applicare una funzione a ogni elemento di una lista
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))  # Applicazione della funzione lambda per elevare al quadrato ogni elemento della lista
print("Numeri al quadrato:", squared_numbers)

# Utilizzo di filter per filtrare gli elementi di una lista in base a una condizione
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Filtraggio degli elementi pari dalla lista
print("Numeri pari:", even_numbers)

# Utilizzo di reduce per ridurre una sequenza di valori ad un singolo valore
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)  # Riduzione della lista moltiplicando tutti gli elementi
print("Prodotto degli elementi:", product)

# Utilizzo di generator expressions per creare generatori di sequenze
squares = (x**2 for x in range(1, 6))  # Creazione di un generatore di numeri al quadrato
print("Generator expression:", list(squares))
