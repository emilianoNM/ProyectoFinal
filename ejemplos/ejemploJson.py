import json
ejemploJson={'nombre':"emiliano", 'edad':29 , 'esProfesor':True,0:{'dato':'ejemplo1','dato1':2}}

print (ejemploJson)
print (ejemploJson['nombre'])
print (ejemploJson[0])
print (ejemploJson[0]['dato'])

for atributo in ejemploJson:
    print(atributo)
    print(ejemploJson[atributo])
    for atributo2 in ejemploJson[0]:
        print atributo2

cadena=json.dumps(ejemploJson)

print cadena

f=open('json.dat','w')

f.write(cadena)

f.close()

f2=open('json.dat','r')

CadenaJson=f2.read()

print CadenaJson

jsonRecuperado=json.loads(CadenaJson)

print jsonRecuperado['nombre']

jsonRecuperado['nombre']='Juan'
jsonRecuperado['edad']=int(jsonRecuperado['edad'])+10
f=open('json.dat','w')

cadena=json.dumps(jsonRecuperado)
f.write(cadena)

f.close()
