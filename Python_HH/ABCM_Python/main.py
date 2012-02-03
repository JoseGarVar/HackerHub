import Empleado
from FuncionesIO import Alta_Empleado


MAX_EMP = 100
Numero_Empleados = 0
Emp = Empleado.Empleado()
op = 6

while(op > 5 or op < 1):

    print "---------------------------------"
    print "1.- Alta de Empleado"
    print "2.- Baja de Empleado"
    print "3.- Consulta de Empleado"
    print "4.- Modificar Empleado"
    print "5.- SALIR"
    op = int(raw_input("Seleccione una Opcion: "))
    print "---------------------------------"




#Altas
    if op == 1:   
        Numero_Empleados = Alta_Empleado(Numero_Empleados,Emp)
    
        op = 6 #Para volver a cargar el menu
        
    
