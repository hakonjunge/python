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



#Oppgave 6
def calculate_shopping_cart_price(shopping_cart, all_wares, tax=0.25):
    handlekurv_sum = 0
    for produkt in shopping_cart:
        antall = shopping_cart[produkt]
        pris = all_wares[produkt]['price']
        handlekurv_sum += antall * pris * tax
    return handlekurv_sum


print(calculate_shopping_cart_price(shopping_cart, all_wares, 0.25))