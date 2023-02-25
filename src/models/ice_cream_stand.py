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
        if self.flavors:
            # refatorando para ter um return
            #print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            return self.flavors
            # for flavor in self.flavors:
            #     print(f"\t-{flavor}")
        else:
            return "Estamos sem estoque atualmente!"
            #print("Estamos sem estoque atualmente!")

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                # bug: está retorenando a lista. Deveria ser somente flavor
                return f"Temos no momento {flavor}!"
                #print(f"Temos no momento {self.flavors}!")
            else:
              return f"Não temos no momento {flavor}!"
                #print(f"Não temos no momento {self.flavors}!")
        else:
            return "Estamos sem estoque atualmente!"
            #print("Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        # bug: não precisa verificar se a lista esta vazia
        #if self.flavors:
        if flavor in self.flavors:
            return "Sabor já disponivel!"
            # print("\nSabor já disponivel!")
        else:
            self.flavors.append(flavor)
            return f"{flavor} adicionado ao estoque!"
            #print(f"{flavor} adicionado ao estoque!")
        #else:
        #    return "Estamos sem estoque atualmente!"
            # print("Estamos sem estoque atualmente!")
