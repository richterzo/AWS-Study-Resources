# File: my_module.py
# Questo è un modulo personalizzato contenente una semplice funzione.

def greet(name):
    return f"Ciao, {name}!"

# File: my_package/__init__.py
# Questo è un file vuoto, ma la presenza di questo file rende la directory my_package un pacchetto Python.

# File: my_package/my_submodule.py
# Questo è un sotto-modulo all'interno del pacchetto.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# File: main.py
# Questo è il file principale del tuo programma, dove utilizzi i moduli e i pacchetti definiti precedentemente.

# Importa il modulo personalizzato
import my_module

# Importa il pacchetto personalizzato e i suoi sotto-moduli
import my_package.my_submodule

# Utilizza la funzione dal modulo personalizzato
print(my_module.greet("Alice"))

# Utilizza le funzioni dal pacchetto e dal suo sotto-modulo
print(my_package.my_submodule.add(5, 3))
print(my_package.my_submodule.subtract(10, 4))
