#codigo criado por: Paulo Vinicius Nunes


from time import sleep
from os import system as sys




sys('cls')


while True:


    print('--------------------------------| CÁLCULO DE IP | --------------------------------\n')
    # Matriz de Valores




    IpNumberFormat = [0,0,0,0]
    BinTab = [128,64,32,16,8,4,2,1]


    # Adesão dos valores dos octetos


    for i in range(0,4):
   
        while True:
       
            IpNumberFormat[i] = int(input('Digite um valor do {}° octeto entre 0 e 255: '.format(i+1)))
       
            if IpNumberFormat[i] < 0 or IpNumberFormat[i] > 255:
           
                print('Invalid Value, write again: ')
                print('\n')
                continue
       
            else:
           
                break


    # Verificação do valor da mascara


    while True:
   
        Mask = int(input('Digite o valor da mascara, de 8 a 32: '))


        if Mask <8 or Mask> 32:
       
            print('Invalid Value, write again: ')
            continue
   
        else:
       
            break


    # Verificação da modificação


    if Mask in range(1,9):
   
        Modificacao = 1
   
    elif Mask in range(9,17):
   
        Modificacao = 2
   
    elif Mask in range(17,25):
   
        Modificacao = 3
   
    else:
   
        Modificacao = 4


#VERIFICAÇÃO MASCARA: FULL ou LESS


    if Mask%8 == 0:
   
        ClassMask = 'FULL'
   
    else:
   
        ClassMask = 'LESS'


#Verificando classe do IP


    if (IpNumberFormat[0] <=127 and IpNumberFormat[1] <= 255 and IpNumberFormat[2] <= 255 and IpNumberFormat[3] <= 255):


        Class = 'A'


    elif (IpNumberFormat[0] >=128 and IpNumberFormat[1] >= 0 and IpNumberFormat[2] >= 0 and IpNumberFormat[3] >= 0) and (IpNumberFormat[0] <=191 and IpNumberFormat[1] <= 255 and IpNumberFormat[2] <= 255 and IpNumberFormat[3] <= 255):


        Class = 'B'


    elif (IpNumberFormat[0] >=192 and IpNumberFormat[1] >= 0 and IpNumberFormat[2] >= 0 and IpNumberFormat[3] >= 0) and (IpNumberFormat[0] <=223 and IpNumberFormat[1] <= 255 and IpNumberFormat[2] <= 255 and IpNumberFormat[3] <= 255):


        Class = 'C'


    elif (IpNumberFormat[0] >= 224 and IpNumberFormat[1] >= 0 and IpNumberFormat[2] >= 0 and IpNumberFormat[3] >= 0) and (IpNumberFormat[0] <=239 and IpNumberFormat[1] <= 255 and IpNumberFormat[2] <= 255 and IpNumberFormat[3] <= 255):


        Class = 'D'


    elif (IpNumberFormat[0] >=240 and IpNumberFormat[1] >= 0 and IpNumberFormat[2] >= 0 and IpNumberFormat[3] >= 0) and (IpNumberFormat[0] <=247 and IpNumberFormat[1] <= 255 and IpNumberFormat[2] <= 255 and IpNumberFormat[3] <= 255):


        Class = 'E'


    else:


        Class = 'E'


    #Verificar se é Privado ou Publico


    if ((IpNumberFormat[0] >=10 and IpNumberFormat[1] >= 0 and IpNumberFormat[2] >= 0 and IpNumberFormat[3] >= 0) and  (IpNumberFormat[0] <=10 and IpNumberFormat[1] <= 255 and IpNumberFormat[2] <= 255 and IpNumberFormat[3] <= 255)) or ((IpNumberFormat[0] >=172 and IpNumberFormat[1] >= 16 and IpNumberFormat[2] >= 0 and IpNumberFormat[3] >= 0) and (IpNumberFormat[0] <=172 and IpNumberFormat[1] <= 31 and IpNumberFormat[2] <= 255 and IpNumberFormat[3] <= 255)) or ((IpNumberFormat[0] >=192 and IpNumberFormat[1] >= 168 and IpNumberFormat[2] >= 0 and IpNumberFormat[3] >= 0) and (IpNumberFormat[0] <=192 and IpNumberFormat[1] <= 168 and IpNumberFormat[2] <= 255 and IpNumberFormat[3] <= 255)):


        TypeIp = 'Privado'


    else:


        TypeIp = 'Público'


    #Transformar Mascara normal em endereço IPv4


    IMF = [0,0,0,0]




    if Mask%8 == 0:
   
        for i in range(0,Mask//8):
       
            IMF[i] = 255
   
   
    else:
   
   
        for i in range(0,Modificacao-1):
       
            IMF[i] = 255
   
        if Mask >= 8:
       
            for j in range(0,(Mask-(Modificacao-1)*8)):
       
                IMF[i+1] = BinTab[j] + IMF[i+1]
           


        elif Mask < 8:
       
            for j in range(0,(Mask)):
       
                IMF[0] = BinTab[j] + IMF[0]
       
   
    # Apresentação das caracteristicas atuais


    print('\n')
    print('--------------------------------| STATUS | --------------------------------\n')


    print('ENDEREÇAMENTO: endereço IPV4 tem a forma {}.{}.{}.{}/{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],IpNumberFormat[3],Mask))
    print('CLASS MASK: {}'.format(ClassMask))


    print('MODIFICAÇÃO: A modificação ocorrera no {}° octeto'.format(Modificacao))
    print('NETMASK: {}.{}.{}.{} = {}'.format(IMF[0],IMF[1],IMF[2],IMF[3],Mask))
    print('\n')


    print('------------------------------ | NETWORK STATISTCS | ------------------------------\n')






    LPASD = input('Digite algo para vizualisar as estatísticas: ')


    print('\n')


    sys('cls')


    print('------------------------------ | NETWORK STATISTCS | ------------------------------\n')


    print('ENDEREÇO: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],IpNumberFormat[3]))
    sleep(0.1)
    print('MÁSCARA DE REDE: {}.{}.{}.{} = {}        CLASS: {}'.format(IMF[0],IMF[1],IMF[2],IMF[3],Mask,ClassMask))
    sleep(0.1)
    print('WILDCARD: {}.{}.{}.{}'.format(255-IMF[0],255-IMF[1],255-IMF[2],255-IMF[3]))
    sleep(0.1)
    print('CLASSE: {}'.format(Class))
    sleep(0.1)
    print('TIPO: {}'.format(TypeIp))
    sleep(0.1)


    #VARIAVEL AUXILIAR A




    for k in range(1,9):


        if Mask == k or Mask == (k+8) or Mask == (k+16) or Mask ==(k+24):


            A = BinTab[k-1]
            break


        else:


            continue




    #REDE


    if Modificacao == 2:


        for l in range(256,-A,-A):


            if IpNumberFormat[1] >= l:


               
           
                if (Mask == 15 and IpNumberFormat[1]%2 == 0) or (Mask == 9 and IpNumberFormat[1] == 128):
               
               
                    print('REDE: {}.{}.0.0'.format(IpNumberFormat[0],l))


                elif ClassMask == 'FULL':


                    print('REDE: {}.{}.0.0'.format(IpNumberFormat[0],IpNumberFormat[1]))
               
                else:


               
               
                    print('REDE: {}.{}.0.0'.format(IpNumberFormat[0],l))
               
                break


            else:


                continue


    elif Modificacao == 3:


        for l in range(256,-A,-A):


            if IpNumberFormat[2] >= l:
           
                l = abs(l)
           
                if (Mask == 23 and IpNumberFormat[2]%2 == 0) or (Mask == 17 and IpNumberFormat[2] == 128):
               
                    print('REDE: {}.{}.{}.0'.format(IpNumberFormat[0],IpNumberFormat[1],l))


                elif ClassMask == 'FULL':


                    print('REDE: {}.{}.{}.0'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2]))
               
                else:
               
                    print('REDE: {}.{}.{}.0'.format(IpNumberFormat[0],IpNumberFormat[1],l))
               
                break


            else:


                continue


    elif Modificacao == 4:


        for l in range(256,-A,-A):


            if IpNumberFormat[3] >= l:
           
           
                if (Mask == 31 and IpNumberFormat[3]%2 == 0) or (Mask == 25 and IpNumberFormat[3] == 128):
           
                    print('REDE: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],l))
                    break


                elif ClassMask == 'FULL':


                    print('REDE: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],IpNumberFormat[3]))
                    break
           
                else:
               
                    print('REDE: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],l))
                    break
               
            else:


                continue


    elif Modificacao == 1:


        for l in range(256,-A,-A):


            print('REDE: {}.0.0.0'.format(IpNumberFormat[0]))
            break
           


    sleep(0.1)


    #PRIMEIRO HOST


    if Modificacao ==2:
   
        if (Mask == 15 and IpNumberFormat[1]%2 == 0) or (Mask == 9 and IpNumberFormat[1] == 128):
       


            print('PRIMEIRO HOST: {}.{}.0.1'.format(IpNumberFormat[0],l))


        elif ClassMask == 'FULL':


            print('PRIMEIRO HOST: {}.{}.0.1'.format(IpNumberFormat[0],IpNumberFormat[1]))
       
        else:
       
            print('PRIMEIRO HOST: {}.{}.0.1'.format(IpNumberFormat[0],l))


    elif Modificacao == 3:
   
   
        if (Mask == 23 and IpNumberFormat[2]%2 == 0) or (Mask == 17 and IpNumberFormat[2] == 128):
       
   
            print('PRIMEIRO HOST: {}.{}.{}.1'.format(IpNumberFormat[0],IpNumberFormat[1],l))


        elif ClassMask == 'FULL':


            print('PRIMEIRO HOST: {}.{}.{}.1'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2]))
       
        else:
       
            print('PRIMEIRO HOST: {}.{}.{}.1'.format(IpNumberFormat[0],IpNumberFormat[1],l))


    elif Modificacao == 4:
   


        if ClassMask == 'FULL':


            print('PRIMEIRO HOST: INEXISTENTE')


        else:


            print('PRIMEIRO HOST: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],l+1))


    elif Modificacao == 1:


        print('PRIMEIRO HOST: {}.0.0.1'.format(IpNumberFormat[0]))




    sleep(0.1)


    #LAST HOST


    if Modificacao == 2:
   
        if (Mask == 15 and IpNumberFormat[1]%2 == 0) or (Mask == 9 and IpNumberFormat[1] == 128):
       


            print('ÚLTIMO HOST: {}.{}.255.254'.format(IpNumberFormat[0],l+A-1))


        elif ClassMask == 'FULL':


            print('ÚLTIMO HOST: {}.{}.255.254'.format(IpNumberFormat[0],IpNumberFormat[1]))
       
        else:
       
            print('ÚLTIMO HOST: {}.{}.255.254'.format(IpNumberFormat[0],l+A-1))


    elif Modificacao == 3:
   
        if (Mask == 23 and IpNumberFormat[2]%2 == 0) or (Mask == 17 and IpNumberFormat[2] == 128):


            print('ÚLTIMO HOST: {}.{}.{}.254'.format(IpNumberFormat[0],IpNumberFormat[1],l+A-1))


        elif ClassMask == 'FULL':


            print('ÚLTIMO HOST: {}.{}.{}.254'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2]))
       
        else:
       
            print('ÚLTIMO HOST: {}.{}.{}.254'.format(IpNumberFormat[0],IpNumberFormat[1],l+A-1))


    elif Modificacao == 4:
   
        if (Mask == 31 and IpNumberFormat[3]%2 == 0) or (Mask == 25 and IpNumberFormat[3] == 128):
       


            print('ÚLTIMO HOST: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],l+A-2))


        elif ClassMask == 'FULL':


            print('ÚLTIMO HOST: INEXISTENTE')
       
        else:
       
            print('ÚLTIMO HOST: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],l+A-2))


    elif Modificacao == 1:


        print('ÚLTIMO HOST: {}.255.255.254'.format(IpNumberFormat[0]))


    sleep(0.1)


    #BROADCAST


    if Modificacao == 2:
   
        if (Mask == 15 and IpNumberFormat[1]%2 == 0) or (Mask == 9 and IpNumberFormat[1] == 128):
       


            print('BROADCAST: {}.{}.255.255'.format(IpNumberFormat[0],l+A-1))


        elif ClassMask == 'FULL':


            print('BROADCAST: {}.{}.255.255'.format(IpNumberFormat[0],IpNumberFormat[1]))
       
        else:
       
            print('BROADCAST: {}.{}.255.255'.format(IpNumberFormat[0],l+A-1))


    elif Modificacao == 3:
   
        if (Mask == 23 and IpNumberFormat[2]%2 == 0) or (Mask == 17 and IpNumberFormat[2] == 128):
       


            print('BROADCAST: {}.{}.{}.255'.format(IpNumberFormat[0],IpNumberFormat[1],l+A-1))


        elif ClassMask == 'FULL':


            print('BROADCAST: {}.{}.{}.255'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2]))
       
        else:
       
            print('BROADCAST: {}.{}.{}.255'.format(IpNumberFormat[0],IpNumberFormat[1],l+A-1))


    elif Modificacao == 4:
   
        if (Mask == 31 and IpNumberFormat[3]%2 == 0) or (Mask == 25 and IpNumberFormat[3] == 128):
       


            print('BROADCAST: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],l+A-1))


        elif ClassMask == 'FULL':


            print('BROADCAST: INEXISTENTE')
       
        else:
       
            print('BROADCAST: {}.{}.{}.{}'.format(IpNumberFormat[0],IpNumberFormat[1],IpNumberFormat[2],l+A-1))
       
    elif Modificacao == 1:


        print('BROADCAST: {}.255.255.255'.format(IpNumberFormat[0]))


    sleep(0.1)


    #TOTAL HOST




   
    print('TOTAL DE HOST: {}'.format(2**(32-Mask)-2))






    if Mask == 31 or Mask == 32:


        print(' ')
        print('OBS: POSSIVELMENTE O PROGRAMA ESTÁ APRESENTANDO SITUAÇÕES ESTRANHAS, ISSO OCORRE POIS A MÁSCARA QUE SELECIONOU É INVALIDADA.')
   




    print(' ')




    Ending = input("Deseja continuar calculando IP's? (S/N): ")


    if Ending == 'S' or Ending == 's' or Ending =='Sim' or Ending == 'sim' or Ending == 'y':


        sys('cls')
        continue


    else:


        break

