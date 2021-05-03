import PySimpleGUI as sg
from billboardpack import billb_window
from goodreads_pack import goodreads_window

def layout():
    layout1 = [
    [sg.Text('¿Que datos analizamos?',  font = ("Helvetica", 14), text_color ='white', pad=(0,10))],
    [sg.Button('Billboard Hot 100', pad=(0,15))],
    [sg.Button('GoodReads', pad=(0,15))],
    [sg.Button('Salir', pad=(0, 10))]

    ]
    ventana = sg.Window('config', layout1, element_justification='c', size=(300,300))

    return ventana

def start ():
    ventana = layout()

    while True:
        events, values = ventana.read()

        if events == sg.WINDOW_CLOSED or events=='Salir':
            break

        if events == 'Billboard Hot 100':
            ventana.hide()
            billb_window.start()
            ventana.un_hide()

        elif events == 'GoodReads':
            ventana.hide()
            goodreads_window.start()
            ventana.un_hide()

    ventana.close()

start()