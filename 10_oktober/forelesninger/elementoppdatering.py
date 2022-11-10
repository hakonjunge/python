import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="PYCHARM", width=600, height=400)

with dpg.window(no_title_bar=True, tag="window"):
    dpg.add_text("Placeholder")
    with dpg.child_window(height=50, width=-1):
        dpg.add_text("Menu")
    with dpg.child_window(height=200, width=-1):
        dpg.add_text("Main")
        with dpg.group(horizontal=True):
            with dpg.child_window(height=-1, width=150):
                dpg.add_text("Files")
            with dpg.child_window(height=-1, width=-1):
                 dpg.add_text("Editor")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)
dpg.start_dearpygui()
dpg.destroy_context()
