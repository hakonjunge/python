all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
        "description": "All the cores and threads you'll need!",
    },

    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
        "description": "Next generation console, never in stock!",
    },

    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable - 2m",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
        "description": "A high speed overprices HDMI cable!",
    }
}


#Oppgave 5
def add_number_to_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    if is_number_of_ware_in_stock(ware, number_of_ware):
        shopping_cart[ware_key] = number_of_ware
    else:
        shopping_cart[ware_key] = ware["number_in_stock"]

shopping_cart = {}

add_number_to_ware_to_shopping_cart("playstation_5", all_wares["playstation_5"],shopping_cart,10)
add_number_to_ware_to_shopping_cart("amd_processor", all_wares["amd_processor"],shopping_cart,10)
add_number_to_ware_to_shopping_cart("hdmi_cable", all_wares["hdmi_cable"],shopping_cart,10)

print(shopping_cart)