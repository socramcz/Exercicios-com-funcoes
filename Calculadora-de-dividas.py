print('-='*22)
print(' '*8, 'CALCULADORA DE DIVIDAS')
print('-='*22)

opcao = input('Para iniciar o programa digite "SIM"\nPara encerrar o programa digite "SAIR"\n=> ').lower()
print('-='*30)

while True:
    if opcao == 'sim':
        saldoDespesas = 0

        salario = float(input('Digite o valor do seu sálario: '))
        contas = int(input('Digite quantas despesas terá que pagar esse mes: '))
        print('-='*30)

        if contas > 0:
            for i in range(contas):
                despesas = int(input(f'Digite o valor da {i+1}º conta: '))
                
                saldoDespesas = despesas + saldoDespesas

            if saldoDespesas < salario:
                valorFinal = salario - saldoDespesas #Calculo para exibir quanto de dinheiro sobrou

                print('-='*30)
                print(f'Voce conseguiu sobreviver esses mês e te sobrou R$ {valorFinal:.2f}')
                print('-='*30)

            elif saldoDespesas == salario:
                print('-='*30)
                print('Voce sobreviveu esse mês, mas não sobrou nada!!')
                print('-='*30)

            else:
                valorFinal = salario - saldoDespesas #Calculo para exibir quanto de dinheiro faltou

                print('-='*30)
                print(f'VISH, esse mês não deu e ficou devendo... tem que reduzir as despesas!!\nFicou com saldo negativo R$ {valorFinal:.2f}')
                print('-='*30)

        else:   #Se caso não tiver nenhuma divida
            print('PARABENS, VOCE ESTÁ EM DIA COM AS CONTAS')

    elif opcao == 'sair' or 'nao': #Para sair do programa
        print(' '*25,'TCHAU')
        print('-='*30)

        break    