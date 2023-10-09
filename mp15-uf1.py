import csv
import json

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

#2

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

# Constants per a les conversions
POLZADES_A_CMS = 2.54
LLIURES_A_KGS = 0.45

# Itera a través de les dades i realitza les conversions d'alçada i pes
for row in data[1:]:  # Ignora la capçalera
    alcada_polzades = float(row[3])
    pes_lliures = float(row[4])
    
    # Realitza les conversions
    alcada_cms = round(alcada_polzades * POLZADES_A_CMS, 2)
    pes_kgs = round(pes_lliures * LLIURES_A_KGS, 2)
    
    # Assigna els nous valors a les columnes d'alçada i pes
    row[3] = alcada_cms
    row[4] = pes_kgs

    #1.4

    # Itera a través de les dades i arrodoneix els valors de l'edat a enters
for row in data[1:]:  # Ignora la capçalera
    edat = float(row[5])
    
    # Arrodoneix l'edat a un enter
    edat_arrodonida = round(edat)
    
    # Assigna el nou valor d'edat a la columna corresponent
    row[5] = str(int(edat_arrodonida))

    #1.5

    # Defineix el nom del nou fitxer CSV amb el separador "^"
new_csv_file = 'basket_players_modified.csv'

# Escriu les dades modificades al nou fitxer CSV amb el separador "^"
with open(new_csv_file, 'w', newline='', encoding='ASCII') as file:
    csv_writer = csv.writer(file, delimiter='^')  # Canvia el separador a "^"
    
    # Escriu l'encapçalament
    csv_writer.writerow(['Name', 'Team', 'Position', 'Heigth', 'Weigth', 'Age'])
    
    # Escriu les dades modificades
    csv_writer.writerows(modified_data)

# 2
# Estadístiques
print("Estadístiques:")

# a) Nom del jugador amb el pes més alt
pes_maxim = 0
nom_jugador_pes_maxim = ""
for row in modified_data:
    pes = float(row[4])
    if pes > pes_maxim:
        pes_maxim = pes
        nom_jugador_pes_maxim = row[0]
print(f"a) Nom del jugador amb el pes més alt: {nom_jugador_pes_maxim} ({pes_maxim} kg)")

# b) Nom del jugador amb l’alçada més petita
alcada_minima = float('inf')
nom_jugador_alcada_minima = ""
for row in modified_data:
    alcada = float(row[3])
    if alcada < alcada_minima:
        alcada_minima = alcada
        nom_jugador_alcada_minima = row[0]
print(f"b) Nom del jugador amb l’alçada més petita: {nom_jugador_alcada_minima} ({alcada_minima} cm)")

# c) Mitjana de pes i alçada de jugador per equip
mitjana_pes_per_equip = {}
mitjana_alcada_per_equip = {}

for row in modified_data:
    equip = row[1]
    pes = float(row[4])
    alcada = float(row[3])
    
    if equip not in mitjana_pes_per_equip:
        mitjana_pes_per_equip[equip] = [pes]
        mitjana_alcada_per_equip[equip] = [alcada]
    else:
        mitjana_pes_per_equip[equip].append(pes)
        mitjana_alcada_per_equip[equip].append(alcada)

for equip, pes in mitjana_pes_per_equip.items():
    mitjana_pes_per_equip[equip] = round(sum(pes) / len(pes), 2)

for equip, alcada in mitjana_alcada_per_equip.items():
    mitjana_alcada_per_equip[equip] = round(sum(alcada) / len(alcada), 2)

print("c) Mitjana de pes per equip:")
for equip, mitjana_pes in mitjana_pes_per_equip.items():
    print(f"{equip}: {mitjana_pes} kg")

print("Mitjana d'alçada per equip:")
for equip, mitjana_alcada in mitjana_alcada_per_equip.items():
    print(f"{equip}: {mitjana_alcada} cm")

# d) Recompte de jugadors per posició
recompte_posicions = {}
for row in modified_data:
    posicio = row[2]
    if posicio in recompte_posicions:
        recompte_posicions[posicio] += 1
    else:
        recompte_posicions[posicio] = 1

print("d) Recompte de jugadors per posició:")
for posicio, recompte in recompte_posicions.items():
    print(f"{posicio}: {recompte} jugadors")

# e) Distribució de jugadors per edat
distribucio_edat = {}
for row in modified_data:
    edat = int(float(row[5]))  # Convertir a float y luego a entero
    if edat in distribucio_edat:
        distribucio_edat[edat] += 1
    else:
        distribucio_edat[edat] = 1

print("e) Distribució de jugadors per edat:")
for edat, recompte in distribucio_edat.items():
    print(f"Edat {edat}: {recompte} jugadors")

#3

json_file = 'basket_players.json'
with open(json_file, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f"Los datos se han convertido a JSON y se han guardado en '{json_file}'.")