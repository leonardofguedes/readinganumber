dic1 = ['zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dic2 = ['onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dic3 = ['dez','vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
dic4 = ['cem']
dic5 = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

while True:
    ask = str(input('Digite um nr: ->')).strip()
    if len(ask) == 1: #for numbers between 0-10
        ask1 = int(ask)
        print(f'O número que você digitou foi {dic1[ask1]}.')
    if len(ask) == 2: #fnb 10-100
        ask1 = int(ask[0])
        ask2 = int(ask[1])
        if ask2 == 0: #10,20,30
            print(f'Seu numero é {dic3[ask1-1]}.')
        if ask1 < 2: #fnb 10-20
            if ask2 != 0:
                print(f'Seu número é {dic2[ask2-1]}.')
        else: #fnb 20-100
            if ask2 != 0:
                print(f'Seu número é {dic3[ask1-1]} e {dic1[ask2]}.')
    if len(ask) == 3: #fnb 100-999
        ask1 = int(ask[0])
        ask2 = int(ask[1])
        ask3 = int(ask[2])
        ask4 = int(ask)
        if ask2 + ask3 == 0:
            if ask1 != 1:
                print(f'Seu número é {dic5[ask1-1]}.')
            if ask4 == 100:
                print(f'Seu número é {dic4[0]}.')
        if ask2 == 0 and ask3 != 0:
            print(f'Seu número é {dic5[ask1-1]} e {dic1[ask3]}.')
        if ask3 == 0 and ask2 != 0:
            print(f'Seu número {dic5[ask1-1]} e {dic3[ask2-1]}.')
        if ask2 != 0 and ask3 != 0:
            print(f'Seu número é {dic5[ask1-1]} e {dic3[ask2-1]} e {dic1[ask3]}.')
