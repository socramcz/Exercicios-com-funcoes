def valorPagamento(prestacao, diasAtraso):
    if diasAtraso == 0:
        valorFinal = prestacao
        return valorFinal

    elif diasAtraso > 0:
        valorFinal = prestacao + (prestacao * 0.03) + ((prestacao * 0.001) * diasAtraso)
        return valorFinal
     
prestacao = 1
print('-=' * 50)

while prestacao != 0:
    prestacao = float(input('Digite o valor da prestação: '))

    if prestacao != 0:
        diasAtraso = int(input('Digite quantos dias está em atraso: '))
        valorFinal = valorPagamento(prestacao, diasAtraso)
        
        print(f'Sua conta deu R$ {valorFinal:.2f}')
        print('-=' * 50)