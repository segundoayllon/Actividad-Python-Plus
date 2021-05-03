import PySimpleGUI as  sg
from billboardpack import mas_num_uno
from billboardpack import mas_apariciones
from billboardpack import top_canciones

def layout():
    layout= [[sg.Button('Artistas con mas #1', pad=(0,15))],
             [sg.Button('Artistas con mas apariciones en el ranking', pad=(0,15))],
             [sg.Button('Canciones con mas semanas en #1', pad=(0,15))],
             [sg.Button('VOLVER')]]
    ventana = sg.Window('analisisBB', layout, element_justification='c', size=(300,300))
    return ventana

def start():
    ventana = layout()
    while True:
        event, values = ventana.read()
        if event == sg.WINDOW_CLOSED or event == 'VOLVER':
            break

        if event == 'Artistas con mas #1':
            ventana.hide()
            mas_num_uno.start()
            ventana.un_hide()

        elif event == 'Artistas con mas apariciones en el ranking':
            ventana.hide()
            mas_apariciones.start()
            ventana.un_hide()

        elif event == 'Canciones con mas semanas en #1':
            ventana.hide()
            top_canciones.start()
            ventana.un_hide()


    ventana.close()