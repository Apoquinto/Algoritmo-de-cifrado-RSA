from random import *

def main(  ):

	RSA( )

def getPrime( limite ):
	# Declaración de variables
	# Llista para almacenar primos
	primos = [ ]
	# Lista sin repetición
	multiplos = set( )
	# Contador de primos
	cont = 0
	
	for i in range( 2, limite + 1 ):
		
		if i not in multiplos:
			# Condición adicional para guardar unicamente a los primos entre 800 y 900
			if( i > 800 and i < 1000 ):
				# Anexo de los candidatos viables
				primos.append( i )
				
				cont += 1
			
			# Guardado de todos los multiplos de i
			multiplos.update( range( i * i, limite + 1, i ) )
	
	return primos[ randint( 0, 28 ) ]

def getE ( phi ):
	
	# e > 1 y mcd( e, phi ) = 1
	limite = 100
	
	multiplos = set()
	
	for i in range( 2, limite + 1 ):
		
		if i not in multiplos:
			# Verificamos que el numero primo no sea un divisor de phi(n)
			if( phi % i != 0 ):
				# Devolvemos el primer primo que cumpla nuestra condición
				return i
			
			# Guardado de todos los multiplos de i
			multiplos.update( range( i * i, limite + 1, i ) )

def getD( phi, e ):
	
	for i in range( 100 ):
		
		d = ( 1 + ( i * phi ) ) / e
		#Comprobación para ver si el número es entero
		if ( ( 1 + ( i * phi ) ) % e == 0 ):
		
			return d

def encrip( e, n, mensaje ):
	#Transformación a binario
	e = bin(e)[2:]

	cont = 2 ** ( len( e ) - 1 )

	respuesta = 1
	
	for i in mensaje:
		#Pasado de elemento del codigo a mensaje
		aux = ord( i ) - 64
		
		for j in e:
			
			if( j == '1' ):
			
				respuesta *= (( ( aux ** cont ) % n ) )
			
			cont = cont // 2
		
		respuesta = respuesta % n
		
		print( respuesta )

def RSA():
	
	p = getPrime( 1000 )
	
	q = getPrime( 1000 )
	
	n = p * q
	
	# Public Key
	
	phi = ( p - 1 ) * ( q - 1 )
	
	e = getE( phi )

	publicKey = [ e, n ]
	
	# Private Key
	
	d = getD( phi, e ) 
	
	privateKey = [ d, n ]
	
	# Encriptación
	
	mensaje = input("Inserte mensaje a encriptar: ")
	
	encrip( 11, 8051, 'T' )
	

if __name__ == '__main__':

    main()
