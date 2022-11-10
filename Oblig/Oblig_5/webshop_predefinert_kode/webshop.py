# ------------------------------------------
# Oppgaver
# ------------------------------------------

#Oppgave 1
def print_ware_information(ware):
    print(f"Name: {ware['name']}\nPrice: {ware['price']},-\n"
          f"Number in stock: {ware['number_in_stock']}\nDescrip"
          f"tion: {ware['description']}")

#print_ware_information(all_wares["amd_processor"])


#Oppgave 2
def calculate_average_ware_rating(ware):
    ye = (sum(ware['ratings']) / len(ware['ratings']))
    return round(ye, 1)

#calculate_average_ware_rating(all_wares["amd_processor"])


#Oppgave 3
def get_all_wares_in_stock(all_wares):
    nyListe = {}
    for produkt in all_wares:
        if all_wares[produkt]['number_in_stock'] > 0:
            nyListe[produkt] = (all_wares[produkt])
    return nyListe

#print(get_all_wares_in_stock(all_wares))


#Oppgave 4
def is_number_of_ware_in_stock(ware, number_of_ware):
    return ware['number_in_stock'] >= number_of_ware

#print(is_number_of_ware_in_stock(all_wares["amd_processor"],45))



#Oppgave 5
def add_number_to_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    if is_number_of_ware_in_stock(ware, number_of_ware):
        shopping_cart[ware_key] = number_of_ware
    else:
        shopping_cart[ware_key] = ware["number_in_stock"]

#shopping_cart = {}

#add_number_to_ware_to_shopping_cart("playstation_5", all_wares["playstation_5"],shopping_cart,10)
#add_number_to_ware_to_shopping_cart("amd_processor", all_wares["amd_processor"],shopping_cart,10)
#add_number_to_ware_to_shopping_cart("hdmi_cable", all_wares["hdmi_cable"],shopping_cart,10)

#print(shopping_cart)


#Oppgave 6
def calculate_shopping_cart_price(shopping_cart, all_wares, tax=0.25):
    handlekurv_sum = 0
    for produkt in shopping_cart:
        antall = shopping_cart[produkt]
        pris = all_wares[produkt]['price']
        handlekurv_sum += antall * pris * tax
    return handlekurv_sum


#print(calculate_shopping_cart_price(shopping_cart, all_wares, 0.25))


def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt
lommebok for å kjøpe en handlevogn.'''


def buy_shopping_cart():
    '''Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.'''


# ------------------------------------------
# Predefinerte funksjoner
# ------------------------------------------
def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False


def clear_shopping_cart(shopping_cart):
    '''Tømmer en handlevogn.'''
    shopping_cart.clear()
