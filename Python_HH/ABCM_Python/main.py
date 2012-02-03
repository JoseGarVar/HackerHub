import Empleado

op = 1

while(op <> 5):
    
    print "Seleccione una Opcion:\n"
    print "---------------------------------"
    print "1.- Alta de Empleado"
    print "2.- Baja de Empleado"
    print "3.- Consulta de Empleado"
    print "4.- Modificar Empleado"
    print "5.- SALIR"
    op = int(raw_input(": "))
    print "---------------------------------"

    #Opcion = { 1 : "Alta de Empleado" , 2 : "Baja de Empleado" , 3 : "Consulta de Empleado" , 4 : "Modificar Empleado"}

    MAX_EMP = 100
    Numero = 1
    Emp = Empleado.Empleado()
    #Emp.Imprimir_Personal()
    #a = Empleado.Empleado("Jose","Garcia Vargas","Ingeniero Mecatronica","4621104829","001")
    #a.Imprimir_Personal()
    #print Opcion[op]

    if op == 1:    
        Numero = raw_input("Ingrese el Numero del Trabajador: ")
        Nombre = raw_input("Ingrese el Nombre del Trabajador: ")
        Apellidos = raw_input("Ingrese los Apellidos del Trabajador: ")
        Profesion = raw_input("Ingrese la Profesion del Trabajador: ")
        Telefono = raw_input("Ingrese el Telefono del Trabajador: ")
        Emp.Alta(Numero,Nombre,Apellidos,Profesion,Telefono)
    
