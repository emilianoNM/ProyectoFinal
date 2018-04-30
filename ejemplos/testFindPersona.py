import findPersona


p1=findPersona.Persona("Emiliano",29)
p1.loadPersonas()

p2=findPersona.Persona("kam",23)

p1.save()
p2.save()

p1.close()
