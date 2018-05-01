import findPersona

findPersona.loadListaPersonas()

p1=findPersona.Persona("Emiliano",29)


p2=findPersona.Persona("kam",23)

p1.save()
p2.save()

findPersona.close()

personaEncontrada=findPersona.findPersona("Persona0afed85e-c340-4bc2-ad7c-5a2840cb2ac3")

print(personaEncontrada.nombre,personaEncontrada.id)