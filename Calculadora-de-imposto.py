def somaImposto(taxaImposto, custo):
    taxaImposto = imposto / 100
    custo = valor

    valorFinal = custo + (custo*taxaImposto)
    return valorFinal

imposto = float(input('Digite o valor do imposto: '))
valor = float(input('Digite o valor do produto: '))

preço = somaImposto(imposto, valor)

print(f'O valor final é R$ {preço}')