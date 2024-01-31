# Introduzione alla programmazione in Python

# Storia di Python
# Python è un linguaggio di programmazione ad alto livello creato da Guido van Rossum e rilasciato per la prima volta nel 1991. Il suo nome è ispirato alla serie televisiva comica britannica "Monty Python's Flying Circus". 
# Python è progettato per essere semplice da leggere e scrivere, con un'ampia comunità di sviluppatori che contribuiscono al suo sviluppo e alla sua crescita.

# Interpretato vs Compilato
# Python è un linguaggio di programmazione interpretato. Ciò significa che il codice sorgente Python viene eseguito direttamente da un interprete Python senza la necessità di essere prima compilato in un linguaggio macchina.
# L'interprete Python traduce il codice sorgente in istruzioni eseguibili una riga alla volta, consentendo una maggiore flessibilità e facilità di sviluppo. Tuttavia, questo può comportare una minore velocità di esecuzione rispetto ai linguaggi compilati.

# Caratteristiche di Python
# Python è noto per la sua sintassi chiara e leggibile, che favorisce la scrittura di codice pulito e manutenibile.
# Supporta diversi paradigmi di programmazione, tra cui la programmazione orientata agli oggetti, la programmazione imperativa e la programmazione funzionale.
# Dispone di una vasta libreria standard che fornisce una serie di moduli e funzioni predefinite per una varietà di scopi, riducendo la necessità di scrivere codice da zero.
# È un linguaggio multi-piattaforma, il che significa che può essere eseguito su una varietà di sistemi operativi, tra cui Windows, macOS e Linux.

# Curiosità su Python
# - La filosofia di Python è enfatizzata nel documento "The Zen of Python", accessibile digitando `import this` nell'interprete Python.
# - Python è ampiamente utilizzato in una vasta gamma di settori, inclusi lo sviluppo web, l'analisi dei dati, l'intelligenza artificiale, l'automazione di sistemi e molto altro ancora.
# - Python è un linguaggio adatto sia per principianti che per esperti, grazie alla sua facilità di apprendimento e alla sua potenza.

# 1. Variabili e tipi di dati
# Le variabili sono contenitori per memorizzare dati. In Python, non è necessario dichiarare esplicitamente il tipo di variabile. I tipi di dati comuni includono interi, float, stringhe e booleani.

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
# Python supporta operazioni matematiche comuni come addizione, sottrazione, moltiplicazione e divisione. Le stringhe possono essere concatenate utilizzando l'operatore '+'.

# Operazioni matematiche
result = age * 2 + 5
print("Risultato:", result)

# Concatenazione di stringhe
greeting = "Ciao, " + name + "!"
print(greeting)

# 3. Controllo del flusso
# Python supporta l'istruzione if-else per il controllo del flusso. È possibile eseguire blocchi di codice in base a condizioni specifiche.

# Istruzione if-else
if age >= 18:
    print("Sei maggiorenne")
else:
    print("Sei minorenne")

# 4. Cicli
# Python supporta cicli for e while per eseguire azioni ripetute. I cicli for sono utilizzati per iterare su sequenze di elementi. Il ciclo while esegue un blocco di codice fintanto che una condizione è vera.

# Ciclo for
for i in range(5):   # Itera da 0 a 4
    print("Numero:", i)

# Ciclo while
count = 0
while count < 5:
    print("Conteggio:", count)
    count += 1

# 5. Funzioni
# Le funzioni sono blocchi di codice riutilizzabili. Accettano input, eseguono operazioni e restituiscono output opzionali.

def square(number):
    """
    Restituisce il quadrato del numero fornito.
    """
    return number ** 2

# Utilizzo della funzione square()
result = square(4)
print("Quadrato di 4:", result)

# 6. Commenti
# I commenti sono testo nel codice che viene ignorato dall'interprete Python. Possono essere utilizzati per fornire spiegazioni e documentazione al codice.

# Questo è un commento singolo
"""
Questo è un commento multilinea. È utile per commentare sezioni di codice più lunghe.
"""

# Speriamo che questa introduzione fornisca una panoramica approfondita della programmazione in Python!
