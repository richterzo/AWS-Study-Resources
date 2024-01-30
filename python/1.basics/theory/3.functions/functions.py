# functions.py

# Introduzione alle funzioni in Python

# Le funzioni sono blocchi di codice riutilizzabili che eseguono un'azione specifica.
# Forniscono una maggiore modularità, organizzazione e riutilizzo del codice.

# Definizione di una funzione
def greet():
    """
    Saluta l'utente con un messaggio di benvenuto.
    """
    return "Ciao! Benvenuto!"

# Chiamata della funzione
print(greet())

# Funzioni con parametri
def greet_user(username):
    """
    Saluta l'utente con il nome fornito.
    
    Args:
        username (str): Il nome dell'utente.
    """
    return "Ciao, " + username + "! Benvenuto!"

# Chiamata della funzione con un argomento
print(greet_user("Alice"))

# Funzioni con valore di ritorno
def add_numbers(a, b):
    """
    Restituisce la somma di due numeri.

    Args:
        a (int): Il primo numero.
        b (int): Il secondo numero.

    Returns:
        int: La somma di a e b.
    """
    return a + b

# Chiamata della funzione con argomenti e utilizzo del valore restituito
result = add_numbers(3, 5)
print("La somma è:", result)

# Funzioni con argomenti predefiniti
def greet_user_default(username="Guest"):
    """
    Saluta l'utente con il nome fornito, default a "Guest" se nessun nome viene fornito.

    Args:
        username (str, optional): Il nome dell'utente. Default è "Guest".
    """
    return "Ciao, " + username + "! Benvenuto!"

# Chiamata della funzione senza argomenti
print(greet_user_default())

# Chiamata della funzione con un argomento
print(greet_user_default("Bob"))

# Funzioni con argomenti arbitrari
def greet_users(*usernames):
    """
    Saluta una lista di utenti.

    Args:
        *usernames (str): Una sequenza di nomi utente.
    """
    greetings = []
    for username in usernames:
        greetings.append("Ciao, " + username + "! Benvenuto!")
    return '\n'.join(greetings)

# Chiamata della funzione con argomenti arbitrari
print(greet_users("Alice", "Bob", "Charlie"))

# Funzioni con argomenti di parole chiave
def describe_pet(name, animal_type="cane"):
    """
    Descrive un animale domestico.

    Args:
        name (str): Il nome dell'animale.
        animal_type (str, optional): Il tipo di animale. Default è "cane".
    """
    return "Il mio " + animal_type + " si chiama " + name + "."

# Chiamata della funzione con argomenti di parole chiave
print(describe_pet(name="Fido"))
print(describe_pet(name="Whiskers", animal_type="gatto"))

# Le funzioni sono fondamentali in Python e forniscono un modo efficace per organizzare e riutilizzare il codice.
