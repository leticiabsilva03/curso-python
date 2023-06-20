for i in range(0,16,3):
    if i == 2:
        print ('i é 2, pulando...')
        continue
    
    if i == 8:
        print ('i é 8, seu else não executará...')
        break
    
    for j in range(1, 3): # número final não é executado
        print (i, j)

else:
    print('For executado com sucesso!') # quando o laço For tem break, o else deste for não é executado. Ele apenas será executado se a condição que executa o break do for não é executada.