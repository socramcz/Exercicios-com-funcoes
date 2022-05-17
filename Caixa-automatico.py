# Escreva uma função que receba o total gasto pelo cliente e a opção de pagamento, que pode ser:
# 1) Opção: a vista com 10% de desconto
# 2) Opção: em duas vezes (preço da etiqueta)
# 3) Opção: de 3 até 10 vezes com 3% de juros ao mês (somente para compras acima de R$ 100,00).

def caixa(pagamento):
    if pagamento == 1:
        valorFinal = gasto - (gasto*0.1)
        print(f'A sua compra de R$ {gasto:.2f} ficou R$ {valorFinal:.2f} com 10% de desconto')

    elif pagamento == 2:
        parcela2x = gasto / 2
        print(f'A sua compra de R$ {gasto:.2f} ficou 2x de R$ {parcela2x:.2f}')

    elif gasto >= 100 and 3 <= pagamento <= 10:
        parcelado = gasto / tipo
        juros = parcelado * 0.03
        valorFinal = parcelado+juros

        print(f'A sua compra de R$ {gasto:.2f} ficou {tipo}x de R$ {valorFinal:.2f} com 3% de juros ao mês') 

    elif gasto < 100 and 3 <= pagamento <= 10:
        print('Desculpe essa parcela não pode ser feita com esse valor !!')

    else:
        print('Numero de parcelas invalidas, tente novamente !!')


print('-=' * 50)
print('Digite o total da gasto da conta:', end=' ')
gasto = float(input())

print('-=' * 50)
print('Escolha a forma de pagamento: \n=> a vista - DIGITE "1" \n=> parcelado 2x (sem juros) - DIGITE "2" \n=> parcelado de 3 ate 10x (com 3% juros ao mês) - DIGITE "(numero da parcelas)" ')
print('-=' * 50)

print('FORMA DE PAGAMENTO:', end=' ')

tipo = int(input())
formaPag = caixa(tipo)

print('-=' * 50)