
# Liste: una sequenza ordinata e modificabile di elementi
# - Utilizzate per rappresentare una sequenza di elementi ordinata e modificabile.
# - Adatte per gestire elenchi di oggetti di diversi tipi.
# - Utilizzate in algoritmi di ordinamento, ricerca e manipolazione di dati.
my_list = [1, 2, 3, 4, 5]
# Metodi utili delle liste
my_list.append(6)  # Aggiunge un elemento alla fine della lista
my_list.insert(0, 0)  # Inserisce un elemento in una posizione specifica
my_list.remove(3)  # Rimuove la prima occorrenza di un elemento
print("Lista:", my_list)
print("Indice di 4:", my_list.index(4))  # Trova l'indice di un elemento
print("Numero di occorrenze di 2:", my_list.count(2))  # Conta le occorrenze di un elemento
my_list.sort()  # Ordina la lista
print("Lista ordinata:", my_list)

# Comprehension delle Liste:
# Le comprehension delle liste consentono di creare nuove liste applicando un'espressione a ciascun elemento di una sequenza.

# Creazione di una lista dei quadrati dei numeri da 1 a 5
squared_numbers = [x ** 2 for x in range(1, 6)]
# La sintassi "[x ** 2 for x in range(1, 6)]" crea una nuova lista contenente i quadrati dei numeri da 1 a 5.
# "x ** 2" è l'espressione applicata a ciascun elemento della sequenza.
print("Lista dei quadrati dei numeri da 1 a 5:", squared_numbers)

# Filtraggio di una lista per ottenere solo i numeri pari
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
# La comprehension "[x for x in numbers if x % 2 == 0]" crea una lista contenente solo i numeri pari presenti nella lista 'numbers'.
# L'espressione "if x % 2 == 0" filtra solo i numeri che sono divisibili per 2 (quindi sono pari).
print("Numeri pari nella lista:", even_numbers)

# Tuple: una sequenza ordinata e immutabile di elementi
# - Utilizzate per rappresentare collezioni di dati immutabili.
# - Adatte per rappresentare costanti, coordinate geografiche, valori di configurazione, ecc.
my_tuple = (1, 2, 3, 4, 5)
print("Indice di 3 nella tupla:", my_tuple.index(3))  # Trova l'indice di un elemento
print("Numero di occorrenze di 2 nella tupla:", my_tuple.count(2))  # Conta le occorrenze di un elemento

# Comprehension delle Tuple:
# Le comprehension delle tuple funzionano in modo simile a quelle delle liste, ma restituiscono una tupla anziché una lista.

# Creazione di una tupla delle coppie di numeri e i loro rispettivi quadrati
number_square_tuples = tuple((x, x ** 2) for x in range(1, 6))
# La sintassi "tuple((x, x ** 2) for x in range(1, 6))" crea una nuova tupla contenente le coppie di numeri e i loro quadrati.
# Ogni elemento della tupla è una tupla (numero, quadrato).
print("Tupla delle coppie di numeri e quadrati:", number_square_tuples)

# Creazione di una tupla dei numeri pari da 1 a 10
even_number_tuple = tuple(x for x in range(1, 11) if x % 2 == 0)
# La comprehension "tuple(x for x in range(1, 11) if x % 2 == 0)" crea una tupla contenente solo i numeri pari da 1 a 10.
# L'espressione "if x % 2 == 0" filtra solo i numeri che sono divisibili per 2.
print("Tupla dei numeri pari da 1 a 10:", even_number_tuple)

# Le comprehension delle liste e delle tuple offrono un modo potente ed elegante per creare nuove sequenze
# in base a condizioni o trasformazioni specifiche sui dati esistenti.

# Dizionari: una collezione non ordinata di coppie chiave-valore
# - Utilizzati per rappresentare associazioni chiave-valore efficienti.
# - Adatti per rappresentare dati strutturati, come informazioni sugli utenti, traduzioni, configurazioni, ecc.
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Dizionari: una collezione non ordinata di coppie chiave-valore
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Metodi utili dei dizionari
print("Chiavi:", my_dict.keys())  # Restituisce una vista delle chiavi
print("Valori:", my_dict.values())  # Restituisce una vista dei valori
print("Elementi:", my_dict.items())  # Restituisce una vista di tuple (chiave, valore)
print("Valore di 'name':", my_dict.get("name"))  # Restituisce il valore associato alla chiave specificata
my_dict.update({"email": "alice@example.com"})  # Aggiunge una nuova coppia chiave-valore o aggiorna un valore esistente
print("Dizionario aggiornato:", my_dict)


# Insiemi: una collezione non ordinata e non indicizzata di elementi unici
# - Utilizzati per rimuovere duplicati da una sequenza e per operazioni matematiche sugli insiemi.
# - Adatti per verificare unicità di elementi, trovare l'intersezione o l'unione di due insiemi, ecc.
my_set = {1, 2, 3, 4, 5}
# Metodi utili degli insiemi
my_set.add(6)  # Aggiunge un elemento all'insieme
my_set.remove(3)  # Rimuove un elemento dall'insieme
print("Insieme:", my_set)
print("Unione con {5, 6, 7}:", my_set.union({5, 6, 7}))  # Restituisce l'unione di due insiemi
print("Intersezione con {4, 5, 6}:", my_set.intersection({4, 5, 6}))  # Restituisce l'intersezione di due insiemi
print("Differenza con {3, 4, 5}:", my_set.difference({3, 4, 5}))  # Restituisce la differenza di due insiemi
