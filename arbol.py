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

def mas_Preguntas(padre):
	#global nodo
	#papa=len(nodo)+1
	#padre.mostrarNodo()
	print "excelente continuemos con mas preguntas para cuando el usuario haya introducido"
	print padre.pregunta,padre.respuesta
	print "no lo olvides tenlas en cuenta"
	pregunta = raw_input("Intruduzca la pregunta por favor\n>:")
	respuesta = raw_input("Introduzcalas posibles respuestas para %s separadas por coma ejemplo si,no,tal vez \n>:" %(pregunta))
	oneR=respuesta.split(',')
	for x in range(len(oneR)):
	#print '',len(nodo)+1,papa,[0],nodo[len(nodo)-1].pregunta,oneR[x],'j'
		padre.nodosHijos.append(len(nodo)+1)
		nodo.append(Nodo(len(nodo)+1,padre.n,[],pregunta,oneR[x],''))
		masPreguntas=raw_input("muy bien ahora dime quieres introducir un resultado para cuando el usuaro haya introducido: %s con respuesta %s\n(Y/N):" %(nodo[len(nodo)-1].pregunta,nodo[len(nodo)-1].respuesta))
		if masPreguntas=='Y':
			resp=raw_input("excelente introduce el resultado\n>:")
			nodo[len(nodo)-1].resultado=resp
		if masPreguntas=='N':		
			mas_Preguntas(nodo[len(nodo)-1])
		

def buscaResultado(respuesta):
	#respuesta.mostrarNodo()
	print "buscando..."
	for x in range(len(nodo)):
		if nodo[x].pregunta==respuesta.pregunta and nodo[x].respuesta==respuesta:
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
		nod.write('Respuesta:'+str(nodo[x].respuesta))
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
	pregunta = raw_input("Introduzca una pregunta\n>:")
	if len(nodo)==1:
		nodo[0].pregunta=pregunta
	respuesta = raw_input("Introduzcalas posibles respuestas para %s separadas por coma ejemplo si,no,tal vez \n>:" %(pregunta))
	oneR=respuesta.split(',')
	for x in range(len(oneR)):
	#print '',len(nodo)+1,papa,[0],nodo[len(nodo)-1].pregunta,oneR[x],'j'
		nodo[len(nodo)-1-x].nodosHijos.append(len(nodo)+1)
		nodo.append(Nodo(len(nodo)+1,papa,[],nodo[len(nodo)-1].pregunta,oneR[x],'NULL'))	 
		masPreguntas=raw_input("muy bien ahora dime quieres introducir un resultado para cuando el usuaro haya introducido: %s con respuesta %s\n(Y/N):" %(nodo[len(nodo)-1].pregunta,nodo[len(nodo)-1].respuesta))
		if masPreguntas=='Y':
			resp=raw_input("excelente introduce el resultado\n>:")
			nodo[len(nodo)-1].resultado=resp
		if masPreguntas=='N':
			#nodo[len(nodo)-1].mostrarNodo()		
			mas_Preguntas(nodo[len(nodo)-1])

	print "excelente ya he aprendido manos a la obra"
	print nodo[0].pregunta
	hijas=buscaHijas(1)
	print "las posibles respuestas son:"
	for x in range(len(hijas)):
		print nodo[hijas[x]-1].respuesta
	print "escriba una\n"
	Respuesta=raw_input()
	#resultadoFinal=buscaResultado(Respuesta)
	#print resultadoFinal
	txt_Nodos()
	



	#mostrarNodos()	
	#resultado = raw_input("Introduzca un resultado para:\n%s Respuesta:%s (si decea seguir introduziendo mas preguntas presione ENTER)" %(pregunta,respuesta))
			#if 'final' in respuesta:
	#		break
	#	except:
	#		print ("error")



nodo=[]
if __name__=="__main__":
	nodo.append(Nodo(1,0,[],"pregunta","respuesta","resultado"))
	main()
