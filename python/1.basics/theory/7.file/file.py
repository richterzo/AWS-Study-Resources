import csv
import json

# Lettura di un file di testo
def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Contenuto del file di testo:")
            print(content)
    except FileNotFoundError:
        print(f"File non trovato: {file_path}")

# Scrittura su un file di testo
def write_text_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
        print(f"Contenuto scritto su {file_path}")

# Lettura di un file CSV
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            print("Contenuto del file CSV:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File non trovato: {file_path}")

# Scrittura su un file CSV
def write_csv_file(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)
        print(f"Dati scritti su {file_path}")

# Lettura di un file JSON
def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print("Contenuto del file JSON:")
            print(data)
    except FileNotFoundError:
        print(f"File non trovato: {file_path}")

# Scrittura su un file JSON
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"Dati scritti su {file_path}")

# Esempio di utilizzo delle funzioni
if __name__ == "__main__":
    # File di testo
    text_content = "Questo è un esempio di contenuto per il file di testo."
    write_text_file("test.txt", text_content)
    read_text_file("test.txt")

    # File CSV
    csv_data = [
        ['Nome', 'Cognome', 'Età'],
        ['Mario', 'Rossi', 30],
        ['Anna', 'Verdi', 25]
    ]
    write_csv_file("test.csv", csv_data)
    read_csv_file("test.csv")

    # File JSON
    json_data = {"nome": "Mario", "cognome": "Rossi", "età": 30}
    write_json_file("test.json", json_data)
    read_json_file("test.json")
