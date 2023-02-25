from src.models.ice_cream_stand import IceCreamStand

lista_sabores = ['Morango', 'Abacaxi', 'Chocolate']
restaurante = 'Reataurando ACB'
cuisine_type = 'Sorveteria'

sorvete = IceCreamStand(restaurante, cuisine_type, lista_sabores)

sorvete.flavors_available()