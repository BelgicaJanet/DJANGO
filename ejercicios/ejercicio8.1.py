
#argumento interesante contador 
def animales(aves,contador):

	print (str(contador)+". "+aves+' vuela y pone huevos')

vector=['condor','colibri','halcon','buitre']
contador = 0

for aves in vector:
	animales(aves,contador)
	contador+=1
	print(' ')
