#variaveis
#Created By: Leonardo V. Silva




class menu():
    def __init__(self):

        self.opc = 9
        self.variavel = None

    def showMenu(self):
        print('\n1 - Tipos de dados em python')
        print('2 - Entrar int')     # 0
        print('3 - Entrar Float')   # 1
        print('4 - Entrar String')  # 2
        print('5 - Entrar Boolean') # 3
        print('6 - Consultar Tipo')
        print('7 - Imprimir')
        print('8 - Sobre')
        print('0 - Sair')

        try:
            self.opc = int(input("Digite uma opção:"))
            pass
        except:
            print('\nOpção Invalida')
            pass

    def input(self,type):
        opc = int(type)
        try:
            if opc == 0:
                self.variavel = int(input('Digite um numero inteiro:'))
            if opc == 1:
                self.variavel = float(input('Digite um decimal:'))
            if opc == 2:
                self.variavel = str(input('Digite uma string:'))
            if opc == 3:
                self.variavel = bool(input('Digite um valor logico:'))
            pass
        except:
            print("\nValor invalido para o tipo!")
            pass
        
        

    def typeScan(self):
        return print('\nTipo do valor:', type(self.variavel) )
        

    def imprime(self):
        try:
            print("\nMetodo 1 usando \",variavel")
            print("a variavel digitado foi ", self.variavel)
        except:
            print("\nNão foi possivel executar o metodo 1")

        try:
            print("\nMetodo 2 usando %s e %variavel")
            print(" a variavel digitado foi %s" %self.variavel)
        except:
            print("\nNão foi possivel executar o metodo 2")

        try:
            print("\nMetodo 3 usando concatenação + variavel")
            print("a variavel digitado foi " + self.variavel)
            
        except:
            print("\nNão foi possivel executar o metodo 3")
        return 

    def tiposPython(self):
        types = f"""
            Palavra Reservada   | Tipos | Exemplo
            int                 | Inteiros  | a = 0,1,2...
            float               | Decimal   | f = 3.125356
            boolean             | Logica    | l = true
            string              | Texto     | s = 'Exemplo de texto'
            """
        print(types)

if __name__ == '__main__':
    inicio = menu()
    while inicio.opc != 0:
        inicio.showMenu()
        if inicio.opc == 1:
            inicio.tiposPython()
        if inicio.opc == 2:
            inicio.input(0)
        if inicio.opc == 3:
            inicio.input(1)
            pass
        if inicio.opc == 4:
            inicio.input(2)
            pass
        if inicio.opc == 5:
            inicio.input(3)
            pass
        if inicio.opc == 6:
            inicio.typeScan()
            pass
        if inicio.opc == 7:
            inicio.imprime()
            pass
    pass
    
    