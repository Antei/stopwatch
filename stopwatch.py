import PySimpleGUI as sg
from time import time

sg.theme('black')
sg.set_options(font='Franklin 18')
layout = [
    [sg.Push(), sg.Image('cross.png', pad=0, enable_events=True, key='-CLOSE-')],
    [sg.VPush()],
    [sg.Text('0', font='Franklin 42', text_color='#AAAAAA', key='-TIME-')],
    [
        sg.Button('СТАРТ', button_color=('#AA0000', '#FFFFFF'), border_width=0, key='-STARTSTOP-'), 
        sg.Button('КРУГ', button_color=('#AA0000', '#FFFFFF'), border_width=0, key='-LAP-')
    ],
    [sg.VPush()]
    ]

window = sg.Window('Simple Stopwatch', 
                   layout, 
                   size=(360, 360),
                   no_titlebar=True,
                   element_justification='center'
                   )

start_time = 0
active = False

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        start_time = time()
        active = True
        window['-STARTSTOP-'].update('СТОП')

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

window.close()