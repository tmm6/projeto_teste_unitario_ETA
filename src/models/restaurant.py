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
        Bug:
        - No retorno da mensagem, o nome do restaurante está referenciando o tipo de comida servida. 
        
        Correção: 
        - Ajuste de digitação nas mensagens de retorno. Trocar o print pelo return.
        - Trocar {self.cuisine_type} por {self.restaurant_name}
        - Trocar print por return
        
        Remoção:
        print(f"Esse restaturante chama {self.cuisine_type} and serve {self.cuisine_type}.")
        print(f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto.")
        """
        msg_describe_restaurant = f"Esse restaurante se chama {self.restaurant_name} e serve {self.cuisine_type}. \n" \
                                  f"Esse restaurante está servindo {self.number_served} consumidores desde que " \
                                  f"está aberto."
        return msg_describe_restaurant

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        """
        Bugs: 
        - Se o restaurante está fechado, self.open deve receber True, que equivale a abrir o restaurante. Se deixar como
        False, o restaurante sempre vai ficar fechado.
        - Número de pessoas servidas está negativo. Não faz sentido ter -2 pessoas atenditas. Neste caso alterar para 0,
         ou não utilizar, pois no contrutor já está definido como 0 pessoas.
         
        Correção:
        - Remover self.number_served = -2
        - Trocar self.open = False por self.open = True
        - Trocar print por return
        
        Remoção:
        self.number_served = -2
        print(f"{self.restaurant_name} agora está aberto!")
        print(f"{self.restaurant_name} já está aberto!")
        """
        if not self.open:
            self.open = True
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        """
        Bugs:
        - Será necessário zerar o número de pessoas servidas ao fechar o restaurante, dado que ao abrir o número de
        pessoas servidas também é fechada? Neste caso a opção é retirar self.number_served = 0.
        
        Correção:
        - Remover self.number_served = 0
        - Trocar print por return
        
        Remover:
        self.number_served = 0
        print(f"{self.restaurant_name} agora está fechado!")
        print(f"{self.restaurant_name} já está fechado!")
        """
        if self.open:
            self.open = False
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        """
        Bugs: 
        - Não tem um retorno para o usuário informando se o número de pessoas servidas foi atualizado.
        
        Correção:
        - Adição do retorno: f"{self.number_served} pessoas foram servidas até o momento!"
        """
        if self.open:
            self.number_served = total_customers
            return f"{self.number_served} pessoas foram servidas até o momento!"
        else:
            return f"{self.restaurant_name} está fechado!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        """
        Bug: 
        - Não está sendo realizado o incremento da quantidade de pessoas. Neste caso pode ser perdido algumas 
        informações. Por exemplo: Em um determinado momento o restaurante atendeu 10 pessoas, após um tempo X foram
        atendidas 2 pessoas. Com self.number_served = more_customers, o self.number que antes seria == a 10 agora será 
        == 2.
        - Não tem um retorno para o usuário informando se o número de pessoas servidas foi atualizado.
        
        Correção:
        - Adição do retorno: f"{self.number_served} pessoas foram servidas até o momento!"
        - Trocar self.number_served = more_customers por self.number_served += more_customers
        
        Remoção:
        self.number_served = more_customers
        """
        if self.open:
            self.number_served += more_customers
            return f"{self.number_served} pessoas foram servidas até o momento!"
        else:
            return f"{self.restaurant_name} está fechado!"

    """
    Criação de um método para validar se a quantidade de clientes é válida.
    """
    def valid_qtd_customers(self, customers):
        return type(customers) == int and customers > 0