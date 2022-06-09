
import this
import ExercicioMoldel
this.opcao = -1

def Menu():
    print('Menu\n\n'         +
          '\n1. Exercicio 01'+
          '\n2. Exercicio 02'+
          '\n3. Exercicio 03'+
          '\n4. Exercicio 04'+
          '\n5. Exercicio 05'+
          '\n0. Sair'        +
          '\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado!')
        elif this.opcao == 1:
            print(ExercicioMoldel.Exercicio01())
        elif this.opcao == 2:
            print("Informe um número")
            num1 = int(input())
            print(ExercicioMoldel.Exercicio02(num1))
        elif this.opcao == 3:
            print('Infome a base do retângulo')
            bas = float(input())
            print('Informe a altura do retângulo')
            alt = float(input())
            print(ExercicioMoldel.Exercicio03(bas, alt))
        elif this.opcao == 4:
            print('informe quantos anos completos que você tem')
            anos = float(input())
            print('Informe a quantidade de meses completos que você tem')
            meses = float(input())
            print('Infome a quantidade de dias completos que você tem')
            dias = float(input())
            print(ExercicioMoldel.Exercicio04(anos, meses, dias))
        else:
            print('Opção informada não é válida')