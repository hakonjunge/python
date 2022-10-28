import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Positioning", width=400, height=300)

with dpg.window(no_title_bar=True):
    with dpg.tab_bar():
        with dpg.tab(label="Tab 1"):
            dpg.add_button(label="I dare you to click", )
        with dpg.tab(label="Tab 2"):
            dpg.add_text("MÅGAMAD", indent=50)


    dpg.add_button(label="Må ha farsa", pos=(300, 150))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()