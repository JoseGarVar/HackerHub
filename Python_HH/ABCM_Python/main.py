import Empleado

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

    #Opcion = { 1 : "Alta de Empleado" , 2 : "Baja de Empleado" , 3 : "Consulta de Empleado" , 4 : "Modificar Empleado"}

    
    #Emp.Imprimir_Personal()
    #a = Empleado.Empleado("Jose","Garcia Vargas","Ingeniero Mecatronica","4621104829","001")
    #a.Imprimir_Personal()
    #print Opcion[op]


#Altas
    if op == 1:   
        Numero_Empleados += 1
        Numero = Numero_Empleados 
        Nombre = raw_input("Ingrese el Nombre del Trabajador: ")
        Apellidos = raw_input("Ingrese los Apellidos del Trabajador: ")
        Profesion = raw_input("Ingrese la Profesion del Trabajador: ")
        Telefono = raw_input("Ingrese el Telefono del Trabajador: ")
        
        Mal = 1
        Red = "No"
        Proy = "NO"
        
        while Mal == 1:
            
            Red = raw_input("Usted cuenta con GitHub (Responda SI/NO):")        
            if Red == "NO":
                Github = "NO"
                Mal = 0
            elif Red <> "NO" and not Red == "SI" or Red <> "SI":
                print "Responda en Mayusculas SI o NO"
                Mal == 1
            elif Red == "SI":
                Github = raw_input("\nDigite su cuenta GitHub: ")
                Mal = 0
        
        Mal = 1        
        
        while Mal == 1:
            
            Red = raw_input("Usted cuenta con Twitter (Responda SI/NO):")        
            if Red == "NO":
                Twitter = "NO"
                Mal = 0
            elif Red <> "NO" and not Red == "SI" or Red <> "SI":
                print "Responda en Mayusculas SI o NO"
                Mal == 1
            elif Red == "SI":
                Twitter = raw_input("\nDigite su cuenta Twitter: ")
                Mal = 0
    
        Mal = 1
          
        while Mal == 1:
            
            Red = raw_input("Usted cuenta con Facebook (Responda SI/NO):")        
            if Red == "NO":
                Facebook = "NO"
                Mal = 0
            elif Red <> "NO" and not Red == "SI" or Red <> "SI":
                print "Responda en Mayusculas SI o NO"
                Mal == 1
            elif Red == "SI":
                Facebook = raw_input("\nDigite su cuenta Facebook: ")
                Mal = 0                
            
        Emp.Alta(Numero,Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook)
    
        op = 6 #Para volver a cargar el menu
        
    
