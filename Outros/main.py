def main():
    resposta = pedir_resposta()
    while resposta != '0':
        operando1 = float(input("""Digite o primeiro operando: """))
        operador = resposta
        operando2 = float(input("""Digite o segundo operando: """))

        match resposta:
            case '1':
                resposta = calcula_soma(operando1, operando2)
                print(f"{operando1} + {operando2} =  {resultado}")

            case '2':
                resposta = calcula_subtracao(operando1, operando2)
                print(f"{operando1} - {operando2} =  {resultado}")

            case '3':
                resposta = calcula_multiplicacao(operando1, operando2)
                print(f"{operando1} x {operando2} =  {resultado}")

            case '4':
                resposta = calcula_divisao(operando1, operando2)
                print(f"{operando1} / {operando2} =  {resultado}")

            case '5':
                resposta = calcula_exponenciacao(operando1, operando2)
                print(f" {operando1} ^{operando2} =  {resultado}")

            case '6':
                resposta = calcula_radiciacao(operando1, operando2)
                print(f"{operando1} √{operando2}=  {resultado}")

            case '7':
                resposta = calcula_divisao_inteira(operando1, operando2)
                print(f"{operando1} // {operando2} =  {resultado}")

            case '8':
                resposta = calcula_resto(operando1, operando2)
                print(f"{operando1} % {operando2} =  {resultado}")

            case _:
                print("Escolha entre as opções disponíveis.")
        resposta = pedir_resposta()


def pedir_resposta():
    resposta = input("""
Escolha uma das opcões abaixo: 
1- Adição
2- Subtração
3- Multiplicação
4- Divisão
5- Exponenciação
6- Radiciação
7- Divisão inteira
8- Resto da divisão
0- Sair
""" )
    return resposta

def calcula_soma(operando1, operando2):
    return operando1 + operando2

def calcula_subtracao(operando1, operando2):
    return operando1 - operando2

def calcula_exponenciacao(operando1, operando2):
    return operando1**operando2

def calcula_radiciacao(operando1, operando2):
    return operando1**(1/operando2)

def calcula_multiplicacao(operando1, operando2):
    return operando1 * operando2   

def calcula_divisao(operando1, operando2):
    if operando2 == 0:
        print("Não é possível dividir por zero.")
        return None
    return operando1 / operando2