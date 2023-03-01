import pytest

from src.models.ice_cream_stand import IceCreamStand


class TestIceCreamStand:
    """
    Utilização de técnica de testes por meio de requisitos
    """
    """
    Utilizando fixture para montar um setup comum a todos os testes.
    """
    @pytest.fixture(autouse=True, scope='function')
    def ice_cream_stand(self):
        # ______________SETUP______________
        restaurant_name = 'Sorveteria dos Deuses'
        cuisine_type = 'Sorveteria'
        flavors_list = ['Tapioca', 'Mousse de Pistache', 'Maracujá']
        ice_cream = IceCreamStand(restaurant_name, cuisine_type, flavors_list)
        return ice_cream
        # yield restaurant
        # _______________TEARDOWN______________

    @pytest.fixture
    def msg_no_flavors(self):
        return 'Estamos sem estoque atualmente!'

    def test_flavors_available(self, ice_cream_stand):
        # Setup
        flavors_list = '\n- Tapioca\n- Mousse de Pistache\n- Maracujá'
        msg_flavors_list = f'No momento temos os seguintes sabores de sorvete disponíveis: {flavors_list}'

        # Chamada
        result = ice_cream_stand.flavors_available()

        # Assert
        assert result == msg_flavors_list

    def test_flavors_available_sem_estoque(self, ice_cream_stand, msg_no_flavors):
        # Setup
        result_flavor_list = []
        ice_cream_stand.flavors = []

        # Chamada
        result = ice_cream_stand.flavors_available()

        # Assert
        assert result == msg_no_flavors
        assert ice_cream_stand.flavors == result_flavor_list

    def test_find_flavor(self, ice_cream_stand):
        # Setup
        flavor = 'Tapioca'
        msg_find_flavor = f'Temos no momento {flavor}!'

        # Chamada
        result = ice_cream_stand.find_flavor(flavor)

        # Assert
        assert result == msg_find_flavor

    def test_find_flavor_sabor_nao_existe(self, ice_cream_stand):
        # Setup
        flavor = 'Limão'
        msg_find_flavor = f'Não temos no momento {flavor}!'

        # Chamada
        result = ice_cream_stand.find_flavor(flavor)

        # Assert
        assert result == msg_find_flavor

    def test_find_flavor_sem_estoque(self, ice_cream_stand, msg_no_flavors):
        # Setup
        flavor = 'Tapioca'
        result_flavor_list = []
        ice_cream_stand.flavors = []

        # Chamada
        result = ice_cream_stand.find_flavor(flavor)

        # Assert
        assert result == msg_no_flavors
        assert ice_cream_stand.flavors == result_flavor_list

    def test_add_flavor(self, ice_cream_stand):
        # Setup
        new_flavor = 'Cupuaçu'
        msg_add_flavor = f'{new_flavor} adicionado ao estoque!'
        index_flavors_list = -1

        # Chamada
        result = ice_cream_stand.add_flavor(new_flavor)

        # Assert
        assert result == msg_add_flavor
        assert ice_cream_stand.flavors[index_flavors_list] == new_flavor

    def test_add_flavor_sabor_ja_existente(self, ice_cream_stand):
        # Setup
        duplicate_flavor = 'Maracujá'
        msg_duplicate_flavor = "Sabor já disponivel!"

        # Chamada
        result = ice_cream_stand.add_flavor('Maracujá')

        # Assert
        assert result == msg_duplicate_flavor
        assert ice_cream_stand.flavors[2] == 'Maracujá'