#clear_output()
class Empleado:
    #Abstraccion de los Objetos Empleado
    
    
    def __init__(self):
        print "Accediendo A la Base de Datos"
        
    def Personal(self,Nombre,Apellidos,Profesion,Telefono):
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Profesion = Profesion
        self.Telefono = Telefono
        return True
        
        
    def Redes(self,Github = "NO",Twitter = "NO",Facebook = "NO"):
        self.Github = Github
        self.Twitter = Twitter
        self.Facebook = Facebook
        return True
        
    def Proyecto(self,NombreP = "",Tipo = "",Tecnologia = "",Repositorio = "",Sitio = "",Contribuidores = ""):
        self.NombreP = NombreP
        self.Tipo = Tipo
        self.Tecnologia = Tecnologia
        self.Repositorio = Repositorio
        self.Sitio = Sitio
        self.Contribuidores = Contribuidores
        return True
        
    def Imprimir_Personal(self):
        print "Nombre:" , self.Nombre , self.Apellidos
        print "Profesion/Ocupacion:" , self.Profesion
        print "Telefono:" ,self.Telefono
        
    def Imprimir_Redes(self):
        print "Github:" , self.Github
        print "Twitter:" , self.Twitter
        print "Facebook:" , self.Facebook
        
    def Imprimir_Proyecto(self):
        print "Nombre del Proyecto:" , self.NombreP
        print "Tipo:" , self.Tipo
        print "Tecnologia:" , self.Tecnologia 
        print "Repositorio:" , self.Repositorio
        print "Sitio:" , self.Sitio
        print "Contribuidores:" , self.Contribuidores 
        
    def Alta(self,Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores,insert):
        if self.Personal(Nombre,Apellidos,Profesion,Telefono) == True and self.Redes(Github,Twitter,Facebook) == True and self.Proyecto(NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores) == True:
            print "---------------------------------"
            print "---------------------------------"
            print "---------------------------------"            
            self.Imprimir_Personal()
            self.Imprimir_Redes()
            self.Imprimir_Proyecto()
            print "---------------------------------"
            print "---------------------------------"
            print "---------------------------------"          
        
            
            Mal = 1
   
        
            while Mal == 1:
                
                Correcto = raw_input("\n\nPara Guardar, Verifique que esten bien los Datos...\n\nEstan bien los Datos? (Responda SI/NO):")        
                if Correcto == "NO":
                    print "Vuelva a dar de Alta un Nuevo Empleado"
                    Mal = 2
                elif Correcto <> "NO" and not Correcto == "SI" or Correcto <> "SI":
                    print "Responda en Mayusculas SI o NO"
                    Mal == 1
                elif Correcto == "SI":
                    self.Agregar_Lista(Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores,insert)
                    print "---------------------------------"
                    print "Alta Satisfactoria\n"
                    print "---------------------------------"                    
                    Mal = 0
                    
        
            
    def Agregar_Lista(self,Nombre,Apellidos,Profesion,Telefono,Github,Twitter,Facebook,NombreP,Tipo,Tecnologia,Repositorio,Sitio,Contribuidores,insert):
        insert.execute({'Nombre': Nombre, 'Apellidos': Apellidos, 'Profesion': Profesion,'Telefono': Telefono,'Github': Github,'Twitter': Twitter,'Facebook': Facebook,'NombreP': NombreP,'Tipo': Tipo,'Tecnologia': Tecnologia,'Repositorio': Repositorio,'Sitio': Sitio,'Contribuidores': Contribuidores})
        

 
 
 #Falta crear funciones alta, baja, etc       
        
#Guardar con una , y cuando se lea se divide

