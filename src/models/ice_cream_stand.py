from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    # trocar o print pelo return
    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        """
        Correção:
        - Trocar print por return.
        - Ajustar a mensagem para retornar a frase e os valores.
        
        Remoção:
        print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
        print("Estamos sem estoque atualmente!")
        for flavor in self.flavors:
            print(f"\t-{flavor}")
        """
        if self.flavors:
            return f'No momento temos os seguintes sabores de sorvete disponíveis: {self.flavors}'
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        """
        Bugs:
        - O método está retornando a lista com todos os sabores. 
        Neste caso deverá ser retornado somente o sabor pesquisado.
        
        Correção:
        - Alterar {self.flavors} por flavor
        
        Remoção:
        print(f"Temos no momento {self.flavors}!")
        print(f"Não temos no momento {self.flavors}!")
        print("Estamos sem estoque atualmente!"        
        """
        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento {flavor}!"
            else:
              return f"Não temos no momento {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        """
        Bugs:
        - Não é necessário verificar se a lista está vazia para adicionar um sabor.
        
        Correção:
        - Alterar print para return.
        - Retirar a verificação se a lista de sabores está vazia.
        
        Remoção:
        print(f"{flavor} adicionado ao estoque!")
        print("\nSabor já disponivel!")
        if self.flavors:
        else:
            print("Estamos sem estoque atualmente!")
        """
        if flavor in self.flavors:
            return "Sabor já disponivel!"
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"
