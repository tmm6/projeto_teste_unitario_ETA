from src.models.ice_cream_stand import IceCreamStand
from src.models.restaurant import Restaurant

# restaurante = Restaurant('Sabor do Nordeste', 'Comida Regional')
# result = restaurante.describe_restaurant()
#
# print(result)
#
# print(restaurante.valid_qtd_customers('2'))
# print(restaurante.valid_qtd_customers(2.6))
# print(restaurante.valid_qtd_customers(2))
# restaurante.open_restaurant()
# print(restaurante.open)
#
# restaurante.open_restaurant()
# restaurante.close_restaurant()

lista_sabores = ['Morango', 'Abacaxi', 'Chocolate']
restaurante = 'Reataurando ACB'
cuisine_type = 'Sorveteria'

sorvete = IceCreamStand(restaurante, cuisine_type, lista_sabores)

resultado = sorvete.flavors_available()
print(resultado)

# resultado = sorvete.find_flavor('Abacaxi')
# print(resultado)
#
# resultado = sorvete.find_flavor('Açaí')
# print(resultado)
#
# sorvete.flavors = []
# resultado = sorvete.find_flavor('Abacaxi')
# print(resultado)
#
# resultado = sorvete.add_flavor('Romeu e Julieta')
# print(resultado)
#
# resultado = sorvete.add_flavor('Romeu e Julieta')
# print(resultado)

#print(*sorvete.flavors)

#print('\nNo momento temos os seguintes sabores de sorvete disponíveis:', *sorvete.flavors, sep = "\n -")
