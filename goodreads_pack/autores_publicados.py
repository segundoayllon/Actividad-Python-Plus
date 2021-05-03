import csv
import json
import PySimpleGUI as sg
from collections import Counter

archivo = open("goodreads_pack/books.csv", "r", encoding='utf8')
csvreader = csv.reader(archivo, delimiter=',')

def autor_mas_libros():
    archivo.seek(0)
    columna = (row[2] for row in csvreader)
    return Counter(columna).most_common(20)

def layout():
    headers = ['Autor', 'Cantidad de libros']
    layout=[[sg.Table(values=autor_mas_libros(),
                      headings= headers,
                      justification = 'left')],
            [sg.Button('VOLVER')]]

    ventana = sg.Window('Autor con mas libros', layout, element_justification='c',size=(300,300))

    return ventana

def start():
    ventana = layout()
    while True:
        event, values = ventana.read()
        if  event == 'VOLVER' or event == sg.WINDOW_CLOSED:
            break
    ventana.close()
