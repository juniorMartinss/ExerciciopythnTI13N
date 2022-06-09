
import this
import Operacoes#acessando a classe operações
this.opcao = -1#Declaração de variável global
this.num1  = 0#Declaração de variável global
this.num2  = 0#Declaração de variável global

def mostrarMenu():
    print('Escolha uma das opções abaixo: \n' +
          '1. Soma \n'                        +
          '2. Subtração \n'                   +
          '3. Divisão \n'                     +
          '4. Multiplicação \n'               +
          '0. Sair \n\n')
    this.opcao = int(input())#Entrada de dados

def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input()) #Convertemdo um texto em um número com vírgula.

def coletarNum2():
    print('Informe o segundo número: ')
    this.num2 = float(input()) #Convertendo um texto em um número com vírgula

def executar():
    while(this.opcao != 0):
        mostrarMenu() #chamando o método que mostra opções para o usuario

        if this.opcao == 1:
            coletarNum1()#pegando o primeiro nuúmero
            coletarNum2()#pegando o segundo número
            print('A soma entre {} e {} = {}'.format(this.num1, this.num2, Operacoes.soma(this.num1, this.num2)))
        elif this.opcao == 2:
            coletarNum1()
            coletarNum2()
            print('A subtração entre {} e {} = {}'.format(this.num1, this.num2, Operacoes.subtrair(this.num1, this.num2)))
        elif this.opcao == 3:
            coletarNum1()
            coletarNum2()
            print('A divisão entre {} e {} = {}'.format(this.num1, this.num2, Operacoes.dividir(this.num1, this.num2)))
        elif this.opcao == 4:
            coletarNum1()
            coletarNum2()
            print('A multiplicação entre {} e {} = {}'.format(this.num1, this.num2, Operacoes.multiplicar(this.num1, this.num2)))
        else:
            print('Obrigado!')
            this.opcao = 0

