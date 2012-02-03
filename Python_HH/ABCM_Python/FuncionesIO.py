
def Alta_Empleado(Numero_Empleados,Emp):
    Numero_Empleados += 1
    Numero = Numero_Empleados 
    Nombre = raw_input("Ingrese el Nombre del Trabajador: ")
    Apellidos = raw_input("Ingrese los Apellidos del Trabajador: ")
    Profesion = raw_input("Ingrese la Profesion del Trabajador: ")
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
                Tipo = raw_input("Tipo de Proyecto (Web, Desktop, Movil): ")
                Tecnologia = raw_input("Tecnologia del Proyecto (Python, Andorid, C++, Etc): ")
                Repositorio = raw_input("Repositorio del Proyecto (Si NO Tiene Repositorio solo de Enter): ")
                Sitio = raw_input("Sitio del Proyecto (Si NO Tiene Sitio solo de Enter): ")
                Contribuidores = raw_input("Contribuidores del Proyecto (Si NO Tiene Contribuidores solo de Enter): ")
                
                if Repositorio == "":
                    Repositorio = "NO"
                    
                if Sitio == "":
                    Sitio = "NO" 
     
                if Contribuidores == "":
                    Contribuidores = "NO"  
                    
                Mal = 0      
          
                
        Emp.Alta(Numero,Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores)    
        
        
        
    return Numero_Empleados