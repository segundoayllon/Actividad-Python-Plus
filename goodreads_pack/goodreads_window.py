import PySimpleGUI as  sg
from goodreads_pack import mejor_puntuados
from goodreads_pack import autores_publicados

def layout():
    layout=[[sg.Button('Libros en español mejor puntuados')],
            [sg.Button('Autores con mas libros publicados')],
            [sg.Button('VOLVER')]]

    ventana = sg.Window('GoodReads ', layout,element_justification='c', size=(300,300))

    return ventana

def start():
    ventana = layout()
    while True:
        event, values = ventana.read()
        if event == sg.WINDOW_CLOSED or event == 'VOLVER':
            break

        if event == 'Libros en español mejor puntuados':
            ventana.hide()
            mejor_puntuados.start()
            ventana.un_hide()

        elif event == 'Autores con mas libros publicados':
            ventana.hide()
            autores_publicados.start()
            ventana.un_hide()

    ventana.close()
