#!/usr/bin/env	python

class Nodo:
	def __init__(self, n,NodoPadre, nodosHijos, pregunta, arista, resultado):
		self.n  = n
		self.nodoPadre = NodoPadre
		self.nodosHijos = nodosHijos
		self.pregunta = pregunta
		self.arista = arista
		self.resultado = resultado
	def mostrarNodo(self):
		print "Nodo 				",self.n
		print "Nodo padre 			",self.nodoPadre
		print "Nodos hijos 			",self.nodosHijos
		print "Pregunta 			",self.pregunta
		print "Arista 				",self.arista
		print "Resultado 			",self.resultado

#x = Nodo(1,0,2,3,pregunta,respuesta)
def mostrarNodos():
	#global nodo
	for x in range(len(nodo)):
		nodo[x].mostrarNodo()
		print "==============================="
def buscaHijas(papa):
	hijas=[]
	for x in range(len(nodo)):
		if nodo[x].nodoPadre==papa:
			hijas.append(nodo[x].n)
	return hijas

def mas_Preguntas(padre):
	#global nodo
	#papa=len(nodo)+1
	#padre.mostrarNodo()

	print "excelente continuemos con mas preguntas para cuando el usuario haya introducido"
	print padre.pregunta,padre.arista
	print "no lo olvides tenlas en cuenta"
	pregunta = raw_input("Intruduzca la pregunta por favor\n>:")
	respuesta = raw_input("Introduzcalas posibles respuestas para %s separadas por coma ejemplo si,no,tal vez \n>:" %(pregunta))
	oneR=respuesta.split(',')
	for x in range(len(oneR)):
	#print '',len(nodo)+1,papa,[0],nodo[len(nodo)-1].pregunta,oneR[x],'j'
		padre.nodosHijos.append(len(nodo)+1)
		nodo.append(Nodo(len(nodo)+1,padre.n,[],pregunta,oneR[x],''))
		masPreguntas=raw_input("muy bien ahora dime quieres introducir un resultado para cuando el usuaro haya introducido: %s con respuesta %s\n(Y/N):" %(nodo[len(nodo)-1].pregunta,nodo[len(nodo)-1].arista))
		if masPreguntas=='Y':
			resp=raw_input("excelente introduce el resultado\n>:")
			nodo[len(nodo)-1].resultado=resp
			#break
		if masPreguntas=='N':		
			mas_Preguntas(nodo[len(nodo)-1])
		

def buscaResultado(respuesta):
	#respuesta.mostrarNodo()
	print "buscando..."
	for x in range(len(nodo)):
		if nodo[x].pregunta==respuesta.pregunta and nodo[x].arista==respuesta:
			print "Resultado encontrado\n"
			return nodo[x].resultado

def txt_Nodos():
	nod = open("Nodos.txt","w")
	for x in range(len(nodo)):
		nod.write('Nodo:	'+str(nodo[x].n))
		nod.write('\n')
		nod.write('Padre:	'+str(nodo[x].nodoPadre))
		nod.write('\n')
		nod.write('Hijos:	'+str(nodo[x].nodosHijos))
		nod.write('\n')
		nod.write('Pregunta:'+str(nodo[x].pregunta))
		nod.write('\n')
		nod.write('Arista:'+str(nodo[x].arista))
		nod.write('\n')
		nod.write('Resultado:'+str(nodo[x].resultado))
		nod.write('\n')
		nod.write ("===============================")
		nod.write('\n')
	nod.close()
def main():
	
	#global nodo
	papa=1
	masPreguntas='N'
	print "Arbol de Desicion"
	#mostrarNodos()
	

	#while True:
	#	try:
	#while True:
	#rais
	pregunta = raw_input("Introduzca una pregunta\n>:")
	if len(nodo)==1:
		nodo[0].pregunta=pregunta
	respuesta = raw_input("Introduzcalas posibles respuestas para %s separadas por coma ejemplo si,no,tal vez \n>:" %(pregunta))
	oneR=respuesta.split(',')
	for x in range(len(oneR)):
	#print '',len(nodo)+1,papa,[0],nodo[len(nodo)-1].pregunta,oneR[x],'j'
		nodo[0].nodosHijos.append(len(nodo)+1)
		#print'nodo padre ',len(nodo)-1
		nodo.append(Nodo(len(nodo)+1,papa,[],nodo[0].pregunta,oneR[x],'NULL'))	 
		masPreguntas=raw_input("muy bien ahora dime quieres introducir un resultado para cuando el usuaro haya introducido: %s con respuesta %s\n(Y/N):" 
			%(nodo[len(nodo)-1].pregunta,oneR[x]))
		if masPreguntas=='Y':
			resp=raw_input("excelente introduce el resultado\n>:")
			nodo[len(nodo)-1].resultado=resp
		if masPreguntas=='N':
			#nodo[len(nodo)-1].mostrarNodo()		
			mas_Preguntas(nodo[len(nodo)-1])

	
	#resultadoFinal=buscaResultado(Respuesta)
	#print resultadoFinal
	txt_Nodos()
	



	#mostrarNodos()	
	#resultado = raw_input("Introduzca un resultado para:\n%s Respuesta:%s (si decea seguir introduziendo mas preguntas presione ENTER)" %(pregunta,respuesta))
			#if 'final' in respuesta:
	#		break
	#	except:
	#		print ("error")
def mostrarRespuestas(padre):
	hijas=buscaHijas(padre)
	for x in range(len(hijas)):
		print nodo[hijas[x]-1].arista
	print 'escriba una>:'

def miPapa(nodo):
	return nodo[nodo].nodoPadre
def busqueda(pregunt,respuest):
	#print 'buscando ',pregunt,respuest
	for x in range(len(nodo)):
		if nodo[x].pregunta==pregunt and nodo[x].arista==respuest and nodo[x].resultado!='NULL':
			return nodo[x].resultado
		if nodo[x].resultado=='NULL':
			return nodo[x].nodosHijos


def nextPregunta(padre):
	nodo[padre].mostrarNodo()
	print nodo[padre].pregunta
	mostrarRespuestas(nodo[padre].n)
	respuesta=raw_input()

	if type(busqueda(nodo[padre].pregunta,respuesta))==list:
		print busqueda(nodo[padre].pregunta,respuesta)[0]-1
		nextPregunta (busqueda(nodo[padre].pregunta,respuesta)[0]-1)
		#extPregunta(busqueda(nodo[padre].pregunta,respuesta))
	else:
		print 'resultados encontrados'
		print busqueda(nodo[padre].pregunta,respuesta)

		


def preguntar():
	print "\n\n\n\n\n\n\n\nexcelente ya he aprendido manos a la obra"
	#print nodo[0].pregunta
	#hijas=buscaHijas(1)
	#print "las posibles respuestas aprendidas son:"
	
	"""for x in range(len(hijas)):
		print nodo[hijas[x]-1].arista
		#print nodo[nodo[x].nodosHijos].arista
	print "escriba una\n>:"
	Respuesta=raw_input()"""
	nextPregunta(0)

nodo=[]
if __name__=="__main__":
	nodo.append(Nodo(1,0,[],"pregunta","respuesta","resultado"))
	main()
	preguntar()
