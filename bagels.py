import random

NUM_DIGITOS=3
MAX_CHANCES=10

def main():
    print('Este es Bagels un juego de logica deductiva')

    while True:
        numeroSecreto=getNumeroSecreto()
        print('Ya tengo el numero secreto')
        print('Tienes {} oportunidades para adivinarlo'.format(MAX_CHANCES))

        chance_num=1

        while chance_num<=MAX_CHANCES:
            chance=''
            while len(chance)!= NUM_DIGITOS or not chance.isdecimal:
                print('Chance #:{}'.format(chance_num))
                chance=input('> ')

            pistas=getPistas(chance,numeroSecreto)
            print(pistas)
            chance_num+=1

            if chance==numeroSecreto:
                break
            if chance_num>MAX_CHANCES:
                print('Se terminaron las oportunidades')
                print('el numero secreto es {}'.format(numeroSecreto))
        
        print('Jugar de nuevo (si o no)')
        if not input('> ').lower().startswith('s'):
            break
    print('Gracias por jugar')

def getNumeroSecreto():
    numeros=list('0123456789')
    random.shuffle(numeros)
    numerosecreto=''
    for i in range(NUM_DIGITOS):
        numerosecreto+=str(numeros[i])
    return numerosecreto

def getPistas(chance,numerosecreto):
    if chance == numerosecreto:
        return 'Numero correcto'
    pistas=[]

    for i in range(len(chance)):
        if chance[i] == numerosecreto[i]:
            pistas.append('Fermi')
        elif chance[i] in numerosecreto:
            pistas.append('Pico')
    if len(pistas)==0:
        return 'Bagels'
    else:
        pistas.sort()
        return ' '.join(pistas)

if __name__=='__main__':
    main()