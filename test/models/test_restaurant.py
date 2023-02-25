import pytest

from src.models.restaurant import Restaurant


class TestRestaurant:

    """
    Utilização de técnica de testes por meio de requisitos
    """
    """
    Utilizando fixture para montar um setup comum a todos os testes.
    """
    @pytest.fixture(autouse=True, scope='function')
    def restaurant(self):
        print('______________SETUP______________')
        restaurant = Restaurant('Sabor do Nordeste', 'Comida Regional')
        return restaurant
        # yield restaurant
        print('_______________TEARDOWN______________')

    def test_describe_restaurant(self, restaurant):
        # Setup
        msg_result_describe = f"Esse restaurante se chama Sabor Do Nordeste e serve Comida Regional. \n" \
                                  f"Esse restaurante está servindo 0 consumidores desde que " \
                                  f"está aberto."

        # Chamada
        result = restaurant.describe_restaurant()

        # Assert
        assert result == msg_result_describe

    def test_open_restaurant_reestaurante_fechado(self, restaurant):
        # Setup
        msg_restaurant_opened = "Sabor Do Nordeste agora está aberto!"

        # Chamada
        result = restaurant.open_restaurant()

        # Assert
        assert result == msg_restaurant_opened

    def test_open_restaurant_reestaurante_aberto(self, restaurant):
        # Setup
        msg_restaurant_opened = "Sabor Do Nordeste já está aberto!"
        restaurant.open = True

        # Chamada
        result = restaurant.open_restaurant()

        # Assert
        assert result == msg_restaurant_opened

    def test_close_restaurant_restaurante_aberto(self, restaurant):
        # Setup
        restaurant.open = True
        msg_restaurant_closed = "Sabor Do Nordeste agora está fechado!"

        # Chamada
        result = restaurant.close_restaurant()

        # Assert
        assert result == msg_restaurant_closed

    def test_close_restaurantrestaurante_fechado(self, restaurant):
        # Setup
        msg_restaurant_closed = "Sabor Do Nordeste já está fechado!"

        # Chamada
        result = restaurant.close_restaurant()

        # Assert
        assert result == msg_restaurant_closed

    def test_set_number_served(self, restaurant):
        # Setup
        number_served = 10
        total_customers = 10
        restaurant.open_restaurant()

        # Chamada
        result = restaurant.set_number_served(total_customers)

        # Assert
        assert restaurant.number_served == number_served
        # assert False

    def test_increment_number_served(self, restaurant):
        # Setup
        number_served = 10
        more_customers = 10
        restaurant.open_restaurant()

        # Chamada
        result = restaurant.increment_number_served(more_customers)

        # Assert
        assert restaurant.number_served == number_served
        # assert False

    @pytest.mark.parametrize('values, results', [('sorvete', False), (2.6, False), (-1, False), (10, True)])
    def test_valid_qtd_customers(self, values, results, restaurant):
        # Chamada
        result = restaurant.valid_qtd_customers(values)

        # Asserts
        assert result is results

