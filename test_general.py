import proveedores
import Entregas_programadas
import pedidos

import pickle

proveedor1=proveedores.Proveedores("Sabritas","#","noe","554343","dsds@example.com","calle ejemplo numero alguno")
proveedor2=proveedores.Proveedores("Doritos","#","noe","554342","dsdsd@example.com","calle ejemplo numero alguno")


proveedor1.save()
proveedor2.save()

proveedor1.close()

proveedor1.load()

proveedorBuscar=proveedores.Search("Sabritas")


print(proveedorBuscar.nombre_p,proveedorBuscar.correo_p)

#pedido

pedido1=pedidos.Pedidos("123","escobas","3")
pedido2=pedidos.Pedidos("124","trapeador","4")

pedido1.save()
pedido2.save()

pedido1.close()

pedido1.load()

pedidoBuscar=pedidos.Search("123")

print("Pedido: " +pedidoBuscar.numero_pedido_e)
print("\n Producto: " +pedidoBuscar.nombre_pp)
print(" cantidad: "+pedidoBuscar.cantidad +"\n")

#Entregas:


#validar pedido

validarPedido=pedidos.Search("123")

print("Pedido: " +validarPedido.numero_pedido_e)
print("\n Producto: " +validarPedido.numero_pedido_e)
print(" cantidad: "+validarPedido.numero_pedido_e +"\n")


#b=open("proveedores1.txt","rb")
#c=pickle.load(b)
#b.close()



