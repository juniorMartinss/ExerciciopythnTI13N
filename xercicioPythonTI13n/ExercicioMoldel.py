
def Exercicio01():
    A = 10
    B = 20
    msg = "Antes da troca: A = {}, B = {}".format(A,B)
    aux = A
    A   = B
    B   = aux
    msg = msg + "\nApós a troca A = {}, B = {}".format(A,B)
    return msg

def Exercicio02(num1):
    return num1 - 1

def Exercicio03(bas, alt):
    return bas * alt

def Exercicio04(anos, meses, dias):
    return (anos * 365) + (meses * 30) + dias