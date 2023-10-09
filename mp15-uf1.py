import csv

# Defineix la ruta al fitxer CSV
csv_file = 'basket_players.csv'

# Inicialitza una llista buida per emmagatzemar les dades
data = []

# Llegeix les dades del fitxer CSV
with open(csv_file, 'r', encoding='ASCII') as file:
    csv_reader = csv.reader(file, delimiter=';')
    # Salta la primera línia ja que conté els encapçalaments
    next(csv_reader)
    # Recorre les files del fitxer CSV i afegeix-les a la llista de dades
    for row in csv_reader:
        data.append(row)
# Defineix una nova llista de dades modificades
modified_data = []

# Aquí pots fer les modificacions desitjades a les dades
# Per exemple, afegim un 10% a l'edat de cada jugador
for row in data:
    name, team, position, height, weight, age = row
    age = float(age) + 10  # Augmentem l'edat en 10 anys
    modified_row = [name, team, position, height, weight, str(age)]
    modified_data.append(modified_row)

# Defineix el nom del nou fitxer CSV
new_csv_file = 'basket_players_modified.csv'

# Escriu les dades modificades al nou fitxer CSV
with open(new_csv_file, 'w', newline='', encoding='ASCII') as file:
    csv_writer = csv.writer(file, delimiter=';')
    # Escriu l'encapçalament
    csv_writer.writerow(['Name', 'Team', 'Position', 'Heigth', 'Weigth', 'Age'])
    # Escriu les dades modificades
    csv_writer.writerows(modified_data)

    # Mostra les dades per pantalla i calcula el recompte de files
for i, row in enumerate(data):
    print(f"Row {i + 1}: {row}")

# Calcula el recompte de número de files total
total_rows = len(data)
print(f"Total de files: {total_rows}")

# Diccionari per a la traducció dels noms de les columnes
traduccio_noms = {
    'Name': 'Nom',
    'Team': 'Equip',
    'Position': 'Posicio',
    'Heigth': 'Alcada',
    'Weigth': 'Pes',
    'Age': 'Edat'
}

# Defineix la ruta del fitxer d'origen i de destí
csv_file_origen = 'basket_players.csv'
csv_file_desti = 'basket_players_catala.csv'

# Llegeix les dades del fitxer CSV d'origen
data = []
with open(csv_file_origen, 'r', encoding='ASCII') as file:
    csv_reader = csv.reader(file, delimiter=';')
    data = list(csv_reader)

# Canvia els noms de les columnes en català a la capçalera
data[0] = [traduccio_noms[col] for col in data[0]]

# Escriu les dades amb la nova capçalera en català al fitxer de destí
with open(csv_file_desti, 'w', newline='', encoding='ASCII') as file:
    csv_writer = csv.writer(file, delimiter=';')
    csv_writer.writerows(data)

# Mostra les dades amb la nova capçalera en català
for i, row in enumerate(data):
    print(f"Row {i + 1}: {row}")

#1.2

import csv

# Diccionari per a la traducció de les demarcacions
traduccio_demarcacions = {
    "Point Guard": "Base",
    "Shooting Guard": "Escorta",
    "Small Forward": "Aler",
    "Power Forward": "Ala-pivot",
    "Center": "Pivot"
}

# Defineix la ruta del fitxer d'origen i de destí
csv_file_origen = 'basket_players_catala.csv'
csv_file_desti = 'basket_players_traduits.csv'

# Llegeix les dades del fitxer CSV d'origen
data = []
with open(csv_file_origen, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=';')
    data = list(csv_reader)

# Tradueix les demarcacions utilitzant el diccionari
for row in data[1:]:  # Ignora la capçalera
    row[2] = traduccio_demarcacions.get(row[2], row[2])  # Utilitza el valor actual si no hi ha traducció

# Escriu les dades amb les demarcacions traduïdes al fitxer de destí
with open(csv_file_desti, 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file, delimiter=';')
    csv_writer.writerows(data)

# Mostra les dades amb les demarcacions traduïdes
for i, row in enumerate(data):
    print(f"Row {i + 1}: {row}")

#1.3

POLZADES_A_CMS = 2.54
LLIURES_A_KGS = 0.45

for i, row in enumerate(data):
    # Converteix les dades d'alçada i pes a nombres de tipus float
    alçada_polzades = float(row[3])
    pes_lliures = float(row[4])
    
    # Realitza les conversions
    alçada_cms = round(alçada_polzades * POLZADES_A_CMS, 2)
    pes_kgs = round(pes_lliures * LLIURES_A_KGS, 2)
    
    # Assigna els nous valors a les columnes d'alçada i pes
    row[3] = alçada_cms
    row[4] = pes_kgs

#1.4

for i, row in enumerate(data):
    # Convierte los datos de altura y peso a números de tipo float
    alcada_polzades = row[3]
    if alcada_polzades != 'Alcada':
        alcada_polzades = float(alcada_polzades)
        alcada_cms = round(alcada_polzades * POLZADES_A_CMS, 2)
    else:
        alcada_cms = 'Alcada'
    pes_lliures = float(row[4])
    edat_anys = float(row[5])
    
    # Realiza las conversiones
    pes_kgs = round(pes_lliures * LLIURES_A_KGS, 2)
    edat_anys = round(edat_anys)
    
    # Asigna los nuevos valores a las columnas de altura, peso y edad
    row[3] = alcada_cms
    row[4] = pes_kgs
    row[5] = edat_anys