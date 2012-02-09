
def Alta_Empleado(Emp,insert):
        Ingresar_Datos()
        Emp.Alta(Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores,insert)    
    

def Baja_Empleado(Emp,delete,and_,User):
    
    Max = Max_Emp(User)    
                    
    NE = Verificar_Numero()                
    #seleccionando el Ususario
    while NE < 0 or NE > Max:
        print "Usuario no Encontrado verifique el Numero de Empleado"
        NE = Verificar_Numero()
        
    select = User.select(and_(User.c.id == NE)) 
    Emp_Select = select.execute()
    Imprimir(Emp_Select)
    Mal = 1        
        
    while Mal == 1:
            
        Seg = raw_input("\n\nEsta Seguro de Querer Borrar este Resgistro (Responda SI/NO):")        
        if Seg == "NO":
            print "\nNINGUN REGISTRO SE BORRO"
            Mal = 0
        elif Seg <> "NO" and not Seg == "SI" or Seg <> "SI":
            print "Responda en Mayusculas SI o NO"
            Mal == 1
        elif Seg == "SI":
            delete = User.delete(and_(User.c.id == NE)) 
            delete.execute()            
            print "\nREGISTRO BORRADO"
            Mal = 0
    
    
    

def Consulta_Empleado(Emp,and_,User):
    
    Max = Max_Emp(User)    
    NE = Verificar_Numero()                
    #seleccionando el Ususario
    while NE < 0 or NE > Max:
        print "Usuario no Encontrado verifique el Numero de Empleado"
        NE = Verificar_Numero()
        
    select = User.select(and_(User.c.id == NE)) 
    Emp_Select = select.execute()
    Imprimir(Emp_Select)
   
def Consulta_Empleado_General(Emp,and_,User):  
    select = User.select() 
    Emp_Select = select.execute()
    Imprimir(Emp_Select)
    
def Consulta_Empleado_Profesion(Emp,and_,User,Prof): 
    select = User.select(and_(User.c.Profesion == Prof)) 
    Emp_Select = select.execute()
    Imprimir(Emp_Select)  
   
def Consulta_Empleado_Tecnologia(Emp,and_,User,Tec): 
    select = User.select(and_(User.c.Tecnologia == Tec)) 
    Emp_Select = select.execute()
    Imprimir(Emp_Select)   
 
 
def Consulta_Empleado_Tipo(Emp,and_,User,Tip):  
    select = User.select(and_(User.c.Tipo == Tip)) 
    Emp_Select = select.execute()
    Imprimir(Emp_Select) 

    
def Modificacion_Empleado(Emp,and_,User,insert):
    Max = Max_Emp(User)    
                        
    NE = Verificar_Numero()                
    #seleccionando el Ususario
    while NE < 0 or NE > Max:
        print "Usuario no Encontrado verifique el Numero de Empleado"
        NE = Verificar_Numero()
            
    select = User.select(and_(User.c.id == NE)) 
    Emp_Select = select.execute()
    print "\nUsuario a Modificar\n"
    Imprimir(Emp_Select)    
    
    print "\n\nIngrese TODOS los Datos Nuevamente)\n"
    Ingresar_Datos()

    
    Mal = 1        
    
    while Mal == 1:
            
            Seg = raw_input("\n\nEsta Seguro de Querer Modificar este Resgistro (Responda SI/NO):")        
            if Seg == "NO":
                    print "\nNINGUN REGISTRO SE MODIFICO"
                    Mal = 0
            elif Seg <> "NO" and not Seg == "SI" or Seg <> "SI":
                    print "Responda en Mayusculas SI o NO"
                    Mal == 1
            elif Seg == "SI":
                    delete = User.delete(and_(User.c.id == NE)) 
                    delete.execute()
                    insert.execute({'id':NE, 'Nombre': Nombre, 'Apellidos': Apellidos, 'Profesion': Profesion,'Telefono': Telefono,'Github': Github,'Twitter': Twitter,'Facebook': Facebook,'NombreP': NombreP,'Tipo': Tipo,'Tecnologia': Tecnologia,'Repositorio': Repositorio,'Sitio': Sitio,'Contribuidores': Contribuidores})
                    print "\nREGISTRO MODIFICADO"
                    Mal = 0

def Max_Emp(User):
    select = User.select()
    Emp_Select = select.execute()
    for row in Emp_Select:
        MAX = row['id']
    print "**** Ingrese un Numero de Empleado MENOR a " + str(MAX) + " ****\n"
    return MAX  

def Imprimir(Emp_Select):
    for row in Emp_Select:
            print "\nNumero de Empleado:",row['id']
            print "Nombre del Trabajador:" ,row['Nombre'], row['Apellidos']
            print "Profesion/Ocupacion:" ,row['Profesion']
            print "Telefono:" ,row['Telefono']
            print "Github:" ,row['Github']
            print "Twitter:" ,row['Twitter']
            print "Facebook:" ,row['Facebook']
            print "Nombre del Proyecto:" ,row['NombreP']
            print "Tipo:" ,row['Tipo']
            print "Tecnologia:" ,row['Tecnologia']
            print "Repositorio:" ,row['Repositorio']
            print "Sitio:" ,row['Sitio']
            print "Contribuidores:" ,row['Contribuidores']    
            
            
def Ingresar_Datos():
        global Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores
        Nombre = raw_input("Ingrese el Nombre del Trabajador: ")
        Apellidos = raw_input("Ingrese los Apellidos del Trabajador: ")
        Profesion = Opciones_Profesiones()
        Telefono = raw_input("Ingrese el Telefono del Trabajador: ")
    
        Mal = 1
        Red = "NO"
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
                        Github = "https://github.com/" + raw_input("\nDigite su Nombre de Usuario GitHub: ")
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
                        Twitter = "https://twitter.com/#!/" + raw_input("\nDigite su Nombre de Usuario Twitter: ")
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
                        Facebook = "http://www.facebook.com/" +  raw_input("\nDigite su Nombre de Usuario Facebook: ")
                        Mal = 0                
            
        #Preguntando por Proyectos Personales
        Mal = 1
        
        while Mal == 1:
            
                Proy = raw_input("Usted Tiene algun Proyecto (Responda SI/NO):")        
                if Proy == "NO":
                        NombreP = "SIN PROYECTO"
                        Tipo = ""
                        Tecnologia = ""
                        Repositorio = ""
                        Sitio = ""
                        Contribuidores = ""
                        Mal = 0
                elif Proy <> "NO" and not Proy == "SI" or Proy <> "SI":
                        print "Responda en Mayusculas SI o NO"
                        Mal == 1
                elif Proy == "SI":
                        NombreP = raw_input("Nombre del Proyecto: ")
                        Tipo = Opciones_Tipo()
                        Tecnologia = Opciones_Tecnologia()
                        Repositorio = raw_input("URL del Repositorio del Proyecto (Si NO Tiene Repositorio solo de Enter): ")
                        Sitio = raw_input("Sitio del Proyecto (Si NO Tiene Sitio solo de Enter): ")
                        Contribuidores = raw_input("Contribuidores del Proyecto (Si NO Tiene Contribuidores solo de Enter): ")
                
                        if Repositorio == "":
                                Repositorio = "NO"
                    
                        if Sitio == "":
                                Sitio = "NO" 
     
                        if Contribuidores == "":
                                Contribuidores = "NO"  
                    
                        Mal = 0
              
              
                        
def Verificar_Numero():
        try:       
                NE = int(raw_input("\nIngrese el Numero de Empleado: "))
        except ValueError:
                NE = -1        
        
        return NE
        

def Opciones_Profesiones():
        print "Selecione una Profesion\n"
        print "1.- Ingeniero en Sistemas"
        print "2.- Ingeniero en Mecatronica"
        print "3.- Licenciado en Administracion"
        print "4.- Licenciado en Comunicacion"
        print "5.- Disenador Web"

        try:
                op2 = int(raw_input("Ingrese una Opcion: "))
        except ValueError:
                op2 = -1               
        #seleccionando el Ususario
        while op2 < 0 or op2 > 5:
                try:
                        op2 = int(raw_input("Opcion Invalida, Vuelva a ingresar una Opcion: "))
                except ValueError:
                        op2 = -1 
                                
        if op2 == 1:
                Profesion = "Ingeniero en Sistemas"
        if op2 == 2:
                Profesion = "Ingeniero en Mecatronica"
        if op2 == 3:
                Profesion = "Licenciado en Administracion"
        if op2 == 4:
                Profesion = "Licenciado en Comunicacion"  
        if op2 == 5:
                Profesion = "Disenador Web"       
        return Profesion


def Opciones_Tipo():
        print "\nSelecione un Tipo de Proyecto\n"
        print "1.- Web"
        print "2.- Desktop"
        print "3.- Mobile"
        print "4.- Console"

        try:
                op2 = int(raw_input("Ingrese una Opcion: "))
        except ValueError:
                op2 = -1               
        #seleccionando el Ususario
        while op2 < 0 or op2 > 4:
                try:
                        op2 = int(raw_input("Opcion Invalida, Vuelva a ingresar una Opcion: "))
                except ValueError:
                        op2 = -1 
                                
        if op2 == 1:
                Tipo = "Web"
        if op2 == 2:
                Tipo = "Desktop"
        if op2 == 3:
                Tipo = "Mobile" 
        if op2 == 4:
                Tipo = "Console"       
        return Tipo


def Opciones_Tecnologia():
        print "\nSelecione la Tecnologia de Desarrollo del Proyecto\n"
        print "1.- Ruby"
        print "2.- JavaScript"
        print "3.- Perl"
        print "4.- Shell"
        print "5.- PHP"
        print "6.- C"
        print "7.- Java"
        print "8.- C++"
        print "9.- Objetive-C"
        print "10.- Android"
        print "11.- Python"
        

        try:
                op2 = int(raw_input("Ingrese una Opcion: "))
        except ValueError:
                op2 = -1               
        #seleccionando el Ususario
        while op2 < 0 or op2 > 11:
                try:
                        op2 = int(raw_input("Opcion Invalida, Vuelva a ingresar una Opcion: "))
                except ValueError:
                        op2 = -1 
                                
        if op2 == 1:
                Tipo = "Ruby"
        if op2 == 2:
                Tipo = "JavaScript"
        if op2 == 3:
                Tipo = "Perl" 
        if op2 == 4:
                Tipo = "Shell"  
        if op2 == 5:
                Tipo = "PHP"
        if op2 == 6:
                Tipo = "C"
        if op2 == 7:
                Tipo = "Java" 
        if op2 == 8:
                Tipo = "C++"  
        if op2 == 9:
                Tipo = "Objetive-C"
        if op2 == 10:
                Tipo = "Android"
        if op2 == 11:
                Tipo = "Python"
                  
        return Tipo

def Opciones_Consultas():
        print "\nSelecione el Tipo Consulta\n"
        print "1.- General"
        print "2.- Numero de Empleado"
        print "3.- Profesiones"
        print "4.- Tecnologia"
        print "5.- Tipo"
        

        try:
                op2 = int(raw_input("Ingrese una Opcion: "))
        except ValueError:
                op2 = -1               
        #seleccionando el Ususario
        while op2 < 0 or op2 > 5:
                try:
                        op2 = int(raw_input("Opcion Invalida, Vuelva a ingresar una Opcion: "))
                except ValueError:
                        op2 = -1 
                                     
        return op2