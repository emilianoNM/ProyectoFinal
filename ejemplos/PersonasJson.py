
ListaPersonas={'12312':{'nombre':'emiliano','edad':12}, '1234':{'nombre':'juan','edad':18}}

print (ListaPersonas['12312'])

ListaPersonas['1234']['nombre']='pedro'

print (ListaPersonas)

ListaPersonas['1235']={'nombre':'Luis', 'edad':10}

print (ListaPersonas)

del (ListaPersonas['1234'])

print ( ListaPersonas)
