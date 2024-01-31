import re

# Funzione per formattare una stringa con il nome e l'età
def format_string(name, age):
    return f"Il nome è {name} e l'età è {age} anni."

# Funzione per cercare una parola in una stringa e contare quante volte appare
def count_word_occurrences(string, word):
    return string.count(word)

# Funzione per sostituire una parola con un'altra in una stringa
def replace_word(string, old_word, new_word):
    return string.replace(old_word, new_word)

# Funzione per dividere una stringa in base a un delimitatore
def split_string(string, delimiter):
    return string.split(delimiter)

# Funzione per trovare tutte le corrispondenze di un pattern utilizzando le espressioni regolari
def find_pattern(string, pattern):
    return re.findall(pattern, string)

# Esempi di utilizzo delle funzioni definite sopra
if __name__ == "__main__":
    # Formattazione di una stringa
    formatted_string = format_string("Alice", 30)
    print(formatted_string)

    # Conteggio delle occorrenze di una parola in una stringa
    sentence = "Questa è una stringa di esempio con parole ripetute."
    word_count = count_word_occurrences(sentence, "parole")
    print("Numero di occorrenze della parola 'parole':", word_count)

    # Sostituzione di una parola in una stringa
    new_sentence = replace_word(sentence, "stringa", "frase")
    print("Stringa con la parola sostituita:", new_sentence)

    # Suddivisione di una stringa in base a un delimitatore
    fruits = "mela,banana,uva,ciliegia"
    fruit_list = split_string(fruits, ",")
    print("Lista di frutta:", fruit_list)

    # Ricerca di corrispondenze utilizzando espressioni regolari
    text = "Questa è una stringa con dei numeri: 12345, 67890, 54321."
    pattern = r'\d+'
    matches = find_pattern(text, pattern)
    print("Corrispondenze trovate:", matches)
