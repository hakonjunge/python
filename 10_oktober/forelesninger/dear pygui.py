import dearpygui.dearpygui as dpg

def calculateAndDisplayMoonWeight():
    user_weight = dpg.get_value("input_weight")
    moon_weight = user_weight/9.807*1.622
    print(moon_weight)

dpg.create_context()
dpg.create_viewport(title="Simple Button Click", width=600, height=400)

with dpg.window(no_title_bar=True, no_move=True, width=600, height=400):
    dpg.add_input_float(label="Your weight on earth", width=200, tag="input_weight")
    dpg.add_button(label="Klikk hvis kriss er en løk", callback=calculateAndDisplayMoonWeight)
    dpg.add_text("Result: ")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
