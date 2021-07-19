# projetos-em-python-
#jogo da velha em python 
import os
import random
#from colorama import Fore, Back, Style

jogarnovamente='s'
jogadas=0
quemjoga=2
maxjogadas=9
vit='n'
velha=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def tela():
    global velha
    global jogadas
    os.system('cls')
    print('   0  1  2')
    print('0:  ' + velha[0][0] + ' |' + velha[0][1] + ' |' + velha[0][2])
    print('   -----------')
    print('1:  ' + velha[1][0] + ' |' + velha[1][1] + ' |' + velha[1][2])
    print('   -----------')
    print('2:  ' + velha[2][0] + ' |' + velha[2][1] + ' |' + velha[2][2])
    print('jogadas: ' + str(jogadas))

def jogadorjoga():
    global jogadas
    global quemjoga
    global maxjogadas
    if quemjoga==2 and jogadas<maxjogadas:
        try:
            l = int(input('linha: '))
            c = int(input('coluna: '))
            while velha[1][c]!= ' ':
                l=int(input('linha: '))
                c=int(input('coluna: '))
            velha[1][c]='X'
            quemjoga=1
            jogadas+=1
        except:
            print('linha ou coluna invalida')
            os.system('pause')
            #vit='n'

def cpujoga():
    global jogadas
    global quemjoga
    global maxjogadas
    if quemjoga==1 and jogadas<maxjogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[1][c]!= ' ':
            l =random.randrange(0,3)
            c =random.randrange(0,3)
        velha[1][c]='O'
        jogadas+=1
        quemjoga=2

def verificarvitoria():
    global velha
    vitoria='n'
    simbolos=['X','O']
    for s in simbolos:
        vitoria='n'
        #verificar linhas
        i1=ic=0
        while i1<3:
            soma=0
            ic=0
            while ic<3:
                if(velha[i1][ic]==s):
                    soma+=1
                ic+=1
            if(soma==3):
                vitoria=s
                break
            i1+=1
        if(vitoria!='n'):
            break
        #verificar colunas
        i1=ic=0
        while ic<3:
            soma=0
            i1=0
            while i1<3:
                if(velha[i1][ic]==s):
                    soma+=1
                i1+=1
            if(soma==3):
                vitoria=s
                break
            ic+=1
        if(vitoria!='n'):
            break
        #verifica diagonal1
        soma=0
        idiag=0
        while idiag<3:
            if(velha[idiag][idiag]==s):
                soma+=1
            idiag+=1
        if(soma==3):
            vitoria=s
            break
        #verificador diagonal
        soma=0
        idiag1=0
        idiagc=0
        while idiagc>=0:
            if(velha[idiag1][idiagc]==s):
                soma+=1
            idiag1+=1
            idiagc-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria

def redefinir():
    global velha
    global jogadas
    global quemjoga
    global maxjogadas
    global vit
    jogadas = 0
    quemjoga = 2
    maxjogadas = 9
    vit = 'n'
    velha = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
while(jogarnovamente=='s'):
    while True:
        tela()
        jogadorjoga()
        cpujoga()
        tela()
        vit=verificarvitoria()
        if(vit!='n')or(jogadas>=maxjogadas):
            break

        print('FIM DE JOGO')
        if(vit=='X' or vit=='O'):
            print('resulta:jogador' + vit + 'venceu')
        else:
            print('resultado:empate')
