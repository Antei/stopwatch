import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('black')
    sg.set_options(font='Franklin 18')
    layout = [
        [sg.Push(), sg.Image('cross.png', pad=0, enable_events=True, key='-CLOSE-')],
        [sg.VPush()],
        [sg.Text('0', font='Franklin 42', text_color='#AAAAAA', key='-TIME-')],
        [
            sg.Button('СТАРТ', button_color=('#AA0000', '#FFFFFF'), border_width=0, key='-STARTSTOP-'), 
            sg.Button('КРУГ', button_color=('#AA0000', '#FFFFFF'), border_width=0, key='-LAP-', visible=False)
        ],
        [sg.Column([[]], key='-LAPS-')],
        [sg.VPush()]
            ]

    return sg.Window('Simple Stopwatch', 
                     layout, 
                     size=(400, 400),
                     no_titlebar=True,
                     element_justification='center'
                    )

window = create_window()

start_time = 0
active = False
lap_amount = 1

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-STARTSTOP-':
        if active:
            # от active до стоп
            active = False
            window['-STARTSTOP-'].update('СБРОС')
            window['-LAP-'].update(visible = False)
        else:
            # от стоп до сброс
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1
            # от стоп до active
            else:
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('СТОП')
                window['-LAP-'].update(visible = True)

    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-'].update(elapsed_time)

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        lap_amount += 1

window.close()