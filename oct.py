def dectoOct(decimal):
    if(decimal > 0):
        dectoOct((int)(decimal/8))
        print(decimal%8, end='')
        
decimal = int(input("nombre: "))
print("Octal: ", end='')
dectoOct(decimal)