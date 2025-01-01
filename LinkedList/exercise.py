class Link:
    def __init__(self, dados):
        self.dados = dados
        self.proxiomo = None
    

class List:

    def __init__ (self):
        self.head = None
    
    def inserirDados (self, dados):

        novo_elemento = Link(dados)

        novo_elemento.next = self.head

        self.head = novo_elemento
    
    def print_ (self):

        data = self.head 

        while  data:
            print(data.dados, end=" -> ")
            data = data.next
        print(None)



teste = List()

teste.inserirDados(1)
teste.inserirDados(2)
teste.inserirDados(3)
teste.inserirDados(4)
teste.inserirDados(5)

teste.print_()


