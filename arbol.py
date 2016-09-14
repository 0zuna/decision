#!/usr/bin/env	python

class Nodo:
	def __init__(self, n,NodoPadre, nodosHijos, pregunta, respuesta, resultado):
		self.n  = n
		self.nodoPadre = NodoPadre
		self.nodosHijos = nodosHijos
		self.pregunta = pregunta
		self.respuesta = respuesta
		self.resultado = resultado
	def mostrarNodo(self):
		print "Nodo 				",self.n
		print "Nodo padre 			",self.nodoPadre
		print "Nodos hijos 			",self.nodosHijos
		print "Pregunta 			",self.pregunta
		print "Respuesta 			",self.respuesta
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
def masPreguntas():
	
def main():
	nodo=[]
	global nodo
	papa=1
	masPreguntas='N'
	print "Arbol de Desicion"
	nodo.append(Nodo(1,0,[],"pregunta","respuesta","resultado"))
	#mostrarNodos()
	

	#while True:
	#	try:
	while masPreguntas=='N':
		pregunta = raw_input("Introduzca una pregunta\n>:")
		if len(nodo)==1:
			nodo[0].pregunta=pregunta
		respuesta = raw_input("Introduzcalas posibles respuestas para %s separadas por coma ejemplo si,no,tal vez \n>:" %(pregunta))
		oneR=respuesta.split(',')
		for x in range(len(oneR)):
		#print '',len(nodo)+1,papa,[0],nodo[len(nodo)-1].pregunta,oneR[x],'j'
			nodo[len(nodo)-1-x].nodosHijos.append(len(nodo)+1)
			nodo.append(Nodo(len(nodo)+1,papa,[],nodo[len(nodo)-1].pregunta,oneR[x],''))	 
			masPreguntas=raw_input("muy bien ahora dime quieres introducir un resultado para cuando el usuaro haya introducido: %s con respuesta %s\n(Y/N):" %(nodo[len(nodo)-1].pregunta,nodo[len(nodo)-1].respuesta))
			if masPreguntas=='Y':
				resp=raw_input("excelente introduce el resultado\n>:")
				nodo[len(nodo)-1].resultado=resp
			if masPreguntas=='N':
				papa=len(nodo)+1
				print "excelente continuemos con mas preguntas para cuando el usuario haya introducido"
				print nodo[len(nodo)-1].pregunta,nodo[len(nodo)-1].respuesta
				print "no lo olvides tomolas en cuenta"

	print "excelente ya he aprendido manos a la obra"
	print nodo[0].pregunta
	hijas=buscaHijas(1)
	print "las posibles respuestas son:"
	for x in range(len(hijas)):
		print nodo[hijas[x]-1].respuesta
	print "escriba una\n"
	Respuesta=raw_input()




	#mostrarNodos()	
	#resultado = raw_input("Introduzca un resultado para:\n%s Respuesta:%s (si decea seguir introduziendo mas preguntas presione ENTER)" %(pregunta,respuesta))
			#if 'final' in respuesta:
	#		break
	#	except:
	#		print ("error")


if __name__=="__main__":
	main()
