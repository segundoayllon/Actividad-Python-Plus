import csv
import json
import PySimpleGUI as  sg
from collections import Counter

archivo = open("billboardpack/charts.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')
next(csvreader)
billboard = {}

'''Funcion que devuelve los diez artistas con mas apariciones en el ranking'''
def mas_apariciones():
    lista = []
    for row in csvreader:
        lista.append(row[3])
    return Counter(lista).most_common(20)

def layout():
    lista_headers=['artista', 'apariciones']

    layout=[[sg.Table(values=mas_apariciones(),
                      headings=lista_headers,
                      auto_size_columns = True,
                      justification = 'right')],
            [sg.Button('VOLVER')]]

    ventana = sg.Window('mostrar', layout, element_justification='c', size=(300,300))

    return ventana

def start():
    ventana = layout()
    while True:
        event, values = ventana.read()
        if  event == 'VOLVER' or event == sg.WINDOW_CLOSED:
            break
    ventana.close()
