import dearpygui.dearpygui as dpg


def additem():
    itemname = dpg.get_value("input_itemname")
    dpg.add_text(itemname, parent="cw-list")


def deleteitem():
    dpg.delete_item("cw-list", children_only=True)


dpg.create_context()
dpg.create_viewport(title="PYCHARM", width=600, height=400)

with dpg.window(no_title_bar=True, tag="window"):
    with dpg.group(horizontal=True):
        dpg.add_text("Item name")
        dpg.add_input_text(width=150, tag="Legg til")
        dpg.add_button(label="button")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("window", True)
dpg.start_dearpygui()
dpg.destroy_context()
