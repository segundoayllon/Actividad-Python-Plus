import csv
import json
import PySimpleGUI as sg

archivo = open("goodreads_pack/books.csv", "r", encoding='utf8')
csvreader = csv.reader(archivo, delimiter=',')

def mejor_puntuacion_epañol():
    archivo.seek(0)
    lista_ordenada = sorted((line for line in csvreader if line[6]=='spa'), key= lambda row: row[3], reverse=True)
    lista_final = []
    for item in lista_ordenada[:20]:
        tupla = (item[1], item[3])
        lista_final.append(tupla)
    return lista_final

def layout():
    headers=['Libro', 'Puntuación']
    layout=[[sg.Table(values= mejor_puntuacion_epañol(),
                      headings= headers,
                      justification='left')],
            [sg.Button('VOLVER')]]

    ventana = sg.Window('mejor puntuacion', layout,element_justification='c', size=(300,300))

    return ventana


def start():
    ventana = layout()
    while True:
        event, values = ventana.read()
        if  event == 'VOLVER' or event == sg.WINDOW_CLOSED:
            break
    ventana.close()
