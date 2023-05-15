
class Memoria:
    def __init__(propria, tamanho): #O init recebe o "tamanho" que define o tamanho da memória em número de endereços.#
        propria.memoria = [0] * tamanho 
    def escrever(propria, endereco, data): #que recebe dois parâmetros: o endereço de memória e o dado a ser armazenado naquele endereço (data).#
        if endereco < 0 or endereco >= len(propria.memoria):
            raise ValueError(f"Endereço inválido: {endereco}")
        if data < 0 or data > 255:
            raise ValueError(f"Dado inválido: {data}")
        propria.memoria[endereco] = data # última linha escreve o dado na posição de memória especificada pelo endereço.#

    def ler(propria, endereco):## ler recebe o endereco.##
        if endereco < 0 or endereco >= len(propria.memoria): ##len verifica se é valido a informação#
            raise ValueError(f"Endereço inválido: {endereco}")
        return propria.memoria[endereco] ## retorna o valor armazenado na posição de memória especificada pelo endereço.##

    def listar(propria):
        for i in range(len(propria.memoria)):
            print(f"Endereço {i}: {propria.memoria[i]}") ##mostra o dado armazenado anteriormente e qual endereço#

    def execute(propria):
        while True:
            operation = input("Digite a operação desejada (R para ler, W para escrever, L para listar ou Q para sair): ")
            if operation.upper() == "Q": #upper deixa a letra selecionada pra maiuscula automaticamente#
                break
            endereco = int(input("Digite o endereço de memória (0 a 15): "))
            if operation.upper() == "R":
                valor = propria.ler(endereco)
                print(f"Valor lido: {valor}")
            elif operation.upper() == "W":
                valor = int(input("Digite o valor a ser escrito (0 a 255): "))
                propria.escrever(endereco, valor)
                print(f"Valor {valor} escrito no endereço {endereco}")
            elif operation.upper() == "L":
                propria.listar()
            else:
                print("Operação inválida. Digite R, W, L ou Q.")
# Cria uma memória de tamanho 16
memoria = Memoria(16)

# Executa o loop de operações
memoria.execute()