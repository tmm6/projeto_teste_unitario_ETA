from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:

    def test_flavors_available(self):
        restaurante_name = 'Sorvete dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = ['Tapioca', 'Açaí', 'Maracujá']
        sorveteria = IceCreamStand(restaurante_name, cuisine_type, flavors_list)

        result = sorveteria.flavors_available()

        assert result == flavors_list
        #assert False

    def test_flavors_available_sem_estoque(self):
        restaurante_name = 'Sorvete dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = []
        sorveteria = IceCreamStand(restaurante_name, cuisine_type, flavors_list)

        result = sorveteria.flavors_available()

        assert result == "Estamos sem estoque atualmente!"
        assert sorveteria.flavors == []
        #assert False

    def test_find_flavor(self):
        restaurante_name = 'Sorvete dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = ['Tapioca', 'Açaí', 'Maracujá']
        sorveteria = IceCreamStand(restaurante_name, cuisine_type, flavors_list)

        result = sorveteria.find_flavor('Tapioca')

        assert result == 'Temos no momento Tapioca!'
        # assert False

    def test_find_flavor_sem_sabor(self):
        restaurante_name = 'Sorvete dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = ['Tapioca', 'Açaí', 'Maracujá']
        sorveteria = IceCreamStand(restaurante_name, cuisine_type, flavors_list)

        result = sorveteria.find_flavor('Cupuaçu')

        assert result == 'Não temos no momento Cupuaçu!'
        # assert False

    def test_find_flavor_sem_estoque(self):
        restaurante_name = 'Sorvete dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = []
        sorveteria = IceCreamStand(restaurante_name, cuisine_type, flavors_list)

        result = sorveteria.find_flavor('Cupuaçu')

        assert result == 'Estamos sem estoque atualmente!'
        assert sorveteria.flavors == flavors_list
        # assert False

    def test_add_flavor(self):
        restaurante_name = 'Sorvete dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = ['Tapioca', 'Açaí', 'Maracujá']
        sorveteria = IceCreamStand(restaurante_name, cuisine_type, flavors_list)

        result = sorveteria.add_flavor('Cupuaçu')

        assert result == "Cupuaçu adicionado ao estoque!"
        assert sorveteria.flavors[3] == 'Cupuaçu'
        # assert False

    def test_add_flavor_com_lista_vazia(self):
        restaurante_name = 'Sorvete dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = []
        sorveteria = IceCreamStand(restaurante_name, cuisine_type, flavors_list)

        result = sorveteria.add_flavor('Cupuaçu')

        assert result == "Cupuaçu adicionado ao estoque!"
        assert sorveteria.flavors[0] == 'Cupuaçu'
        # assert False

    def test_add_flavor_ja_existente(self):
        restaurante_name = 'Sorvete dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = ['Tapioca', 'Açaí', 'Maracujá']
        sorveteria = IceCreamStand(restaurante_name, cuisine_type, flavors_list)

        result = sorveteria.add_flavor('Maracujá')

        assert result == "Sabor já disponivel!"
        assert sorveteria.flavors[2] == 'Maracujá'
        # assert False