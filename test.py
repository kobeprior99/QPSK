from  nicegui import ui
with ui.row():

    with ui.link('NiceGUI', 'https://nicegui.io'):
        ui.image('control.png')
    with ui.link('NiceGUI', 'https://nicegui.io', new_tab=True):
        ui.image('Simulate.png')
ui.run()