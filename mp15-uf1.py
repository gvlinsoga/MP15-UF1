
import csv
with open('basket_players.csv', 'r') as csvfile:
    dades = csv.reader(csvfile, delimiter=';')
    for fila in dades:
        nom = fila[0]
        team = fila[1]
        position = fila[2]
        height = fila[3]
        weight = fila[4]
        edat = fila[5]
        print(nom, team, position, height, weight, edat)