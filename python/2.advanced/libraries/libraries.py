# Librerie Python

# NumPy per operazioni matematiche su array e matrici
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Array NumPy:", arr)

# pandas per la manipolazione e l'analisi dei dati
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("DataFrame pandas:")
print(df)

# TensorFlow per il machine learning e l'intelligenza artificiale
import tensorflow as tf
print("Versione TensorFlow:", tf.__version__)

# Django per lo sviluppo web
import django
print("Versione Django:", django.__version__)

# Flask per lo sviluppo di applicazioni web leggere
import flask
print("Versione Flask:", flask.__version__)

# matplotlib per la visualizzazione dei dati
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('Asse x')
plt.ylabel('Asse y')
plt.title('Grafico di esempio')
plt.show()
