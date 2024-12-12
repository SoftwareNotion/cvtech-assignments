from nicegui import ui
import os
import time

class Calc:
    def __init__(self):
        self.amount = 10

calc = Calc

def openCalc():
    for x in range(round(Calc.amount)):
        time.sleep(0.5)
        os.system("start explorer shell:appsfolder\\Microsoft.WindowsCalculator_8wekyb3d8bbwe!App")

with ui.row():
    with ui.card():
        ui.markdown('######Calc (Slang)')
        lockSwitch = ui.switch("Unlock").props()
        ui.button('Open Calc', on_click=lambda: openCalc()).bind_visibility_from(lockSwitch, 'value')
        calcSlider = ui.slider(min=0, max=100, step=1, value=10).props('label').bind_value(Calc, "amount")
    with ui.card():
        ui.markdown('######PassLock')
        ui.knob(min=0, max=9, step=1, value=1, show_value=True, track_color='grey-2')
        
ui.run(native=True, title="Calc (Slang)")