class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        """
        Correção: Ajuste de digitação nas mensagens de retorno. Trocar o print pelo return.
        """
        print(f"Esse restaturante chama {self.cuisine_type} and serve {self.cuisine_type}.")
        print(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        """
        Bugs: 
        - Se o restaurante está fechado, self.open deve receber True, que equivale a abrir o restaurante. Se deixar como
        False, o restaurante sempre vai ficar fechado.
        - Número de pessoas servidas está negativo. Não faz sentido ter -2 pessoas atenditas. Neste caso alterar para 0,
         ou não utilizar, pois no contrutor já está definido como 0 pessoas.
        """
        if not self.open:
            self.open = False
            self.number_served = -2
            print(f"{self.restaurant_name} agora está aberto!")
        else:
            print(f"{self.restaurant_name} já está aberto!")

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        """
        Bugs:
        - Será necessário zerar o número de pessoas servidas ao fechar o restaurante, dado que ao abrir o número de
        pessoas servidas também é fechada? Neste caso a opção é retirar self.number_served = 0.
        """
        if self.open:
            self.open = False
            self.number_served = 0
            print(f"{self.restaurant_name} agora está fechado!")
        else:
            print(f"{self.restaurant_name} já está fechado!")

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        """
        Bug: Não tem um retorno para o usuário informando se o número de pessoas servidas foi atualizado.
        """
        if self.open:
            self.number_served = total_customers
        else:
            print(f"{self.restaurant_name} está fechado!")

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        """
        Bug: 
        - Não está sendo realizado o incremento da quantidade de pessoas. Neste caso pode ser perdido algumas 
        informações. Por exemplo: Em um determinado momento o restaurante atendeu 10 pessoas, após um tempo X foram
        atendidas 2 pessoas. Com self.number_served = more_customers, o self.number que antes seria == a 10 agora será 
        == 2.         
        """
        if self.open:
            self.number_served = more_customers
        else:
            print(f"{self.restaurant_name} está fechado!")
