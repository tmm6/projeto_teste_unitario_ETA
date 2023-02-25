from src.models.restaurant import Restaurant


class TestRestaurant:

    def test_describe_restaurant(self):
        # Setup
        restaurant = Restaurant('Sabor do Nordeste', 'Comida Regional')
        msg_result_decribe = "Esse restaturante chama Sabor do Nordeste and serve Comida Regional."

        # Chamada
        result = restaurant.describe_restaurant()

        # Assert
        assert result == msg_result_decribe

    def test_open_restaurant(self):
        # Setup
        restaurant = Restaurant('Sabor do Nordeste', 'Comida Regional')
        msg_restaurant_opened = "Sabor do Nordeste agora está aberto!"

        # Chamada
        result = restaurant.open_restaurant()

        # Assert
        assert result == msg_restaurant_opened

    def test_close_restaurant(self):
        # Setup
        restaurant = Restaurant('Sabor do Nordeste', 'Comida Regional')
        msg_restaurant_closed = "Sabor do Nordeste agora está fechado!"

        # Chamada
        result = restaurant.close_restaurant()

        # Assert
        assert result == msg_restaurant_closed

    def test_set_number_served(self):
        # Setup
        restaurant = Restaurant('Sabor do Nordeste', 'Comida Regional')
        number_served = 10
        total_customers = 10
        restaurant.open_restaurant()

        # Chamada
        result = restaurant.set_number_served(total_customers)

        # Assert
        assert restaurant.number_served == number_served
        # assert False

    def test_increment_number_served(self):
        # Setup
        restaurant = Restaurant('Sabor do Nordeste', 'Comida Regional')
        number_served = 10
        more_customers = 10
        restaurant.open_restaurant()

        # Chamada
        result = restaurant.increment_number_served(more_customers)

        # Assert
        assert restaurant.number_served == number_served
        # assert False
