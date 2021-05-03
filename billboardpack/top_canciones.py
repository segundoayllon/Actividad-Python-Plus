import csv
import json
import PySimpleGUI as  sg
from collections import Counter

archivo = open("billboardpack/charts.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')
next(csvreader)

def top_canciones():
    canciones = (filter(lambda line: line[1] == "1", csvreader))
    lista=[]
    for row in canciones:
        lista.append(row[2])
    return Counter(lista).most_common(20)

def layout():
    headers=['Cancion','Semanas']
    layout=[[sg.Table(values=top_canciones(),
                      headings=headers,
                      justification='right')],
            [sg.Button('VOLVER')]]

    ventana = sg.Window('top canciones', layout,element_justification='c',size=(300,300))
    return ventana

def start():
    ventana = layout()
    while True:
        event, values = ventana.read()
        if event == sg.WINDOW_CLOSED or event == 'VOLVER':
            break
    ventana.close()