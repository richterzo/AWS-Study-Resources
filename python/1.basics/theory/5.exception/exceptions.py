# Gestione delle eccezioni in Python

# Esempio di una funzione che gestisce varie eccezioni
def handle_exceptions(x, y):
    """
    Esegue operazioni su due numeri e gestisce diverse eccezioni.

    Args:
        x (int): Il primo numero.
        y (int): Il secondo numero.

    Returns:
        float: Il risultato dell'operazione.
    """
    try:
        result = x / y
        return result
    except ZeroDivisionError as e:
        print(f"Errore: Impossibile dividere per zero: {e}")
        return None
    except TypeError as e:
        print(f"Errore: Tipo di dati non supportato: {e}")
        return None
    except Exception as e:
        print(f"Errore generico: {e}")
        return None

# Esempio di utilizzo di diverse eccezioni
def example_exceptions():
    """
    Esempio di utilizzo delle eccezioni.
    """
    # Eccezione per divisione per zero
    result1 = handle_exceptions(10, 0)
    if result1 is not None:
        print("Risultato 1:", result1)
    else:
        print("Errore nel calcolo del risultato 1.")

    # Eccezione per tipo di dati non supportato
    result2 = handle_exceptions(10, 'a')
    if result2 is not None:
        print("Risultato 2:", result2)
    else:
        print("Errore nel calcolo del risultato 2.")

    # Eccezione generica
    result3 = handle_exceptions(10, [2, 3])
    if result3 is not None:
        print("Risultato 3:", result3)
    else:
        print("Errore nel calcolo del risultato 3.")

if __name__ == "__main__":
    example_exceptions()
