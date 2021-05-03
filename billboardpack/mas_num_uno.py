import csv
import json
import PySimpleGUI as  sg
from collections import Counter

archivo = open("billboardpack/charts.csv", "r")
csvreader = csv.reader(archivo, delimiter=',')
next(csvreader)

def mas_num_uno():
    num1 = (filter(lambda line: line[1] == "1", csvreader))
    lista2 = []#[row for row in (num1, row[3])]
    for i in num1:
        lista2.append(i[3])
    return Counter(lista2).most_common(20)

def layout():
    headers=['Artista','Cantidad de #1']

    layout=[[sg.Table(values=mas_num_uno(),
                      headings=headers,
                      justification ='right')],
            [sg.Button('VOLVER')]]

    ventana = sg.Window('#1', layout, element_justification='c', size=(300,300))
    return ventana

def start():
    ventana = layout()
    while True:
        event, values = ventana.read()
        if event == sg.WINDOW_CLOSED or event == 'VOLVER':
            break
    ventana.close()