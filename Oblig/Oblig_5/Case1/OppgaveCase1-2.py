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

#Oppgave 1
def print_ware_information(ware):
    print(f"Name: {ware['name']}\nPrice: {ware['price']},-\n"
          f"Number in stock: {ware['number_in_stock']}\nDescrip"
          f"tion: {ware['description']}")

print_ware_information(all_wares["amd_processor"])


#Oppgave 2
def calculate_average_ware_rating(ware):
    ye = (sum(ware['ratings']) / len(ware['ratings']))
    return round(ye, 1)

calculate_average_ware_rating(all_wares["amd_processor"])


#Oppgave 3
def get_all_wares_in_stock(all_wares):
    nyListe = {}
    for produkt in all_wares:
        if all_wares[produkt]['number_in_stock'] > 0:
            nyListe[produkt] = (all_wares[produkt])
    return nyListe

print(get_all_wares_in_stock(all_wares))


#Oppgave 4
def is_number_of_ware_in_stock(ware, number_of_ware):
    return ware['number_in_stock'] >= number_of_ware

print(is_number_of_ware_in_stock(all_wares["amd_processor"],45))


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


#Oppgave 6
def calculate_shopping_cart_price(shopping_cart, all_wares, tax=0.25):
    handlekurv_sum = 0
    for produkt in shopping_cart:
        antall = shopping_cart[produkt]
        pris = all_wares[produkt]['price']
        handlekurv_sum += antall * pris * tax
    return handlekurv_sum


print(calculate_shopping_cart_price(shopping_cart, all_wares, 0.25))
