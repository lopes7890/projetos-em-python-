print('caixa registradora')
print('-' * 30)
tot = 0
cont = ' '
cartao = 0
totc = 0
data = input('data de hoje: ')
while True:
    opcao = int(input('''digite sua opcao:
    [1] dinheiro
    [2] cartao
    opcao =  '''))
    iniciar = str(input('produto:  '))
    valor = float(input('preco: '))
    recebido = float(input('valor recebido: '))
    calculo = recebido - valor
    print(f'troco {calculo}')
    tot += valor
    cont += iniciar
    if opcao == 2:
        cartao += 1
        totc += valor
    resp = ' '
    while resp not in 'sn':
        print('ATENCAO DIGITE n SO SE FOR FECHAR O CAIXA')
        resp = str(input('iniciar nova venda? [s/n] '))
print('-' * 30)
print('RELATORIO DO DIA {}'.format(data))
print(f'voce recebeu {tot} hoje e {totc} foi no cartao')
print('voce vendeu {}'.format(cont))
saida = ''
while saida not in 'sn':
    saida = input('deseja sair? [s/n]')
    if saida == s:
        break
